import cv2
import math
import numpy as np
import mediapipe as mp
import keyboard
from colorMatch import get_closest_color, get_broad_color, process_card
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
killStatus = False
normalizeColor = False
def killColorCap():
    global killStatus
    killStatus = True
def normalizeColorFunc():
    global normalizeColor
    normalizeColor = True
def runColorCap():
    mp_hands = mp.solutions.hands
    url = "http://192.168.1.171:8080/video"
    cap = cv2.VideoCapture(0)
    rDiff, gDiff, bDiff = 0, 0, 0
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        rDiff = 0
        gDiff = 0
        bDiff = 0
        blackV = 0
        global killStatus
        global normalizeColor
        print("Starting...")
        smoothed_color_bgr = None
        while cap.isOpened():

            if killStatus == True:
                break
            success, image = cap.read()

            if not success:
                print("Empty Frame Input.")
                continue
            
            image = cv2.flip(image, 1)
            alpha = 1
            beta = 0
            image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

            image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            image_hsv[:, :, 1] = cv2.add(image_hsv[:, :, 1], 0)
            image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)
            frame_width = image.shape[1]
            rect_width = frame_width // 4
            aspect_ratio = 2.5 / 3.5
            rect_height = int(rect_width / aspect_ratio)

            top_left = (0, 0)
            bottom_right = (rect_width, rect_height)
            cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), thickness=2)
            if normalizeColor == True:
                blackHSV, whiteBGR = process_card(image, top_left, bottom_right, 20)
                normalizeColor = False
                maxBGR = 255
                rDiff = maxBGR - whiteBGR[2]
                gDiff = maxBGR - whiteBGR[1]
                bDiff = maxBGR - whiteBGR[0]
                blackV = blackHSV[2]
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
                    h, w, _ = image.shape
                    tipx, tipy = int(tip.x * w), int(tip.y * h)
                    dipx, dipy = int(dip.x * w), int(dip.y * h)

                    disp = 50
                    dx = tipx - dipx
                    dy = tipy - dipy
                    mag = math.sqrt(dx**2 + dy**2)
                    if mag == 0:
                        udx, udy = 0, 0
                    else:
                        udx = dx / mag
                        udy = dy / mag
                    dispx = udx * disp
                    dispy = udy * disp

                    pointX = int(tipx + dispx)
                    pointY = int(tipy + dispy)

                    extension = 15
                    x1 = pointX - extension
                    y1 = pointY - extension
                    x2 = pointX + extension
                    y2 = pointY + extension

                    x1 = max(x1, 0)
                    y1 = max(y1, 0)
                    x2 = min(x2, w)
                    y2 = min(y2, h)

                    roi = image[y1:y2, x1:x2]

                alpha = 0.6
                if roi.size > 0:
                    avg_bgr = np.mean(roi, axis=(0, 1))

                    if smoothed_color_bgr is None:
                        smoothed_color_bgr = avg_bgr
                    else:
                        smoothed_color_bgr = alpha * avg_bgr + (1 - alpha) * smoothed_color_bgr
                    cv2.rectangle(image, (0, 0), (50, 50), smoothed_color_bgr.astype(int).tolist(), -1)

                    r, g, b = smoothed_color_bgr[2] + rDiff, smoothed_color_bgr[1] + gDiff, smoothed_color_bgr[0] + bDiff
                    if r > 255:
                        r = 255
                    if g > 255:
                        g = 255
                    if b > 255:
                        b = 255
                        
                    HSV = cv2.cvtColor(np.uint8([[[b, g, r]]]), cv2.COLOR_BGR2HSV)[0][0]
                    h, s, v = HSV[0], HSV[1], HSV[2]
                    v -= blackV
                    bgr2 = cv2.cvtColor(np.uint8([[[h,s,v]]]), cv2.COLOR_HSV2BGR)[0][0]
                    avgBGR = ((0.80 * bgr2.astype(np.float32)) + (0.20 * smoothed_color_bgr.astype(np.float32))).astype(np.uint8)
                    avgHSV = cv2.cvtColor(np.uint8([[[avgBGR[0], avgBGR[1], avgBGR[2]]]]), cv2.COLOR_BGR2HSV)[0][0]
                    hue = (avgHSV[0])*2
                    saturation = ((avgHSV[1])*100)//255
                    value = ((v)*100)//255
                    if value < 0:
                        value = 0            
                    
                    cv2.rectangle(image, (0, 50), (50, 100), cv2.cvtColor(np.uint8([[[h, s, v]]]), cv2.COLOR_HSV2BGR)[0][0].astype(int).tolist(), -1)

                    cv2.rectangle(image, (0, 100), (50, 150), cv2.cvtColor(np.uint8([[[avgHSV[0], avgHSV[1], avgHSV[2]]]]), cv2.COLOR_HSV2BGR)[0][0].astype(int).tolist(), -1)
                    print(f"{avgHSV[0]}, {avgHSV[1]}, {avgHSV[2]} | {h}, {s}, {v}")

                    color_nameHSV = get_broad_color(int(hue), int(saturation), int(value))

                    # color_name, distance = get_closest_color(avgBGR[2], avgBGR[1], avgBGR[0])
                    cv2.putText(image, f"{color_nameHSV}", (x2, y1+50), 0, 1, 0, 3, -1)
                    # cv2.putText(image, f"Af: {round(r)}, {round(g)}, {round(b)}", (x2, y1+100), 0, 0.5, 0, 2, -1)
                    # cv2.putText(image, f"Be: {round(r)}, {round(g)}, {round(b)}, + {rDiff}, {gDiff}, {bDiff}", (x2, y1+100), 0, 0.5, 0, 2, -1)
                    # cv2.putText(image, f"H {round(hue)}, S {round(saturation)}, V {round(value)}", (x2, y1+80), 0, 0.5, 0, 2, -1)
                    cv2.circle(image, (int((x1+x2)/2) , int((y1+y2)/2)), int(extension/2), (0,255,0), 2, -1)
            cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)
            cv2.imshow('Hand Tracking', image)
            if cv2.waitKey(5) & 0xFF == 27:
                cap.release()
                cv2.destroyAllWindows()
        cap.release()
        cv2.destroyAllWindows()
        killStatus = False
