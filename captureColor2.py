import cv2
import numpy as np
import base64
import io
from flask import Flask, request, jsonify
from PIL import Image
import mediapipe as mp
import math
import json

# Initialize Flask app
app = Flask(__name__)

# Initialize MediaPipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Hand detection model
hands = mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Helper function to decode the image data
def decode_image(frame_data):
    img_data = base64.b64decode(frame_data.split(",")[1])  # Remove the base64 prefix
    img = Image.open(io.BytesIO(img_data))
    img = np.array(img)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Processing endpoint for receiving webcam frames
@app.route("/process_frame", methods=["POST"])
def process_frame():
    data = request.get_json()
    frame_data = data["frame"]  # Frame data received from frontend

    # Decode the image
    image = decode_image(frame_data)

    # Process the image using your existing OpenCV logic
    modImage = image
    image = cv2.flip(image, 1)
    cv2.rectangle(image, (100, 0), (200, 100), (255, 0, 0), 5)
    cv2.rectangle(image, (250, 0), (350, 100), (0, 255, 0), 5)
    cv2.rectangle(image, (400, 0), (500, 100), (0, 0, 255), 5)

    # Convert to RGB for MediaPipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    # Process the hand landmarks and extract the index finger tip
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the coordinates for the index finger tip (landmark 8) and dip (landmark 7)
            tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
            # Convert normalized coordinates to pixel values
            h, w, _ = image.shape
            tipx, tipy = int(tip.x * w), int(tip.y * h)
            dipx, dipy = int(dip.x * w), int(dip.y * h)
            # Calculate direction vector and the extended point
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

            # Define the size of the extended box
            extension = 10  # Adjust as needed
            x1 = pointX - extension
            y1 = pointY - extension
            x2 = pointX + extension
            y2 = pointY + extension

            # Ensure the bounding box coordinates are within the image boundaries
            x1 = max(x1, 0)
            y1 = max(y1, 0)
            x2 = min(x2, w)
            y2 = min(y2, h)

            # Crop the region of interest (ROI)
            roi = image[y1:y2, x1:x2]

        top_n = 20  # Number of top vibrant pixels to average
        alpha = 0.6  # Smoothing factor for temporal averaging (0 < alpha <= 1)

        # Calculate the brightest and most saturated color within the ROI
        if roi.size > 0:  # Ensure ROI is not empty
            # Convert ROI to HSV color space
            roi_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

            # Calculate the average color in BGR format
            avg_bgr = np.mean(roi, axis=(0, 1))  # Average over height and width dimensions

            # Apply temporal smoothing
            if smoothed_color_bgr is None:
                smoothed_color_bgr = avg_bgr
            else:
                smoothed_color_bgr = alpha * avg_bgr + (1 - alpha) * smoothed_color_bgr
            modImage = cv2.add(image, np.array([bDiff, gDiff, rDiff], dtype=np.uint8))

            RGB = np.array([smoothed_color_bgr[2], smoothed_color_bgr[1], smoothed_color_bgr[0]])
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
            # avgBGR = ( (smoothed_color_bgr.astype(np.float32) + bgr2.astype(np.float32)) / 2).astype(np.uint8)
            avgHSV = cv2.cvtColor(np.uint8([[[avgBGR[0], avgBGR[1], avgBGR[2]]]]), cv2.COLOR_BGR2HSV)[0][0]
            # h2, s2, v2 = avgHSV[0], avgHSV[1], avgHSV[2]
            hue = (avgHSV[0])*2
            saturation = ((avgHSV[1])*100)//255
            value = ((v)*100)//255
            # value = v
            if value < 0:
                value = 0            
            
            cv2.rectangle(image, (0, 50), (50, 100), cv2.cvtColor(np.uint8([[[h, s, v]]]), cv2.COLOR_HSV2BGR)[0][0].astype(int).tolist(), -1)

            cv2.rectangle(image, (0, 100), (50, 150), cv2.cvtColor(np.uint8([[[avgHSV[0], avgHSV[1], avgHSV[2]]]]), cv2.COLOR_HSV2BGR)[0][0].astype(int).tolist(), -1)
            print(f"{avgHSV[0]}, {avgHSV[1]}, {avgHSV[2]} | {h}, {s}, {v}")

            color_nameHSV = get_broad_color(int(hue), int(saturation), int(value))

            color_name, distance = get_closest_color(avgBGR[2], avgBGR[1], avgBGR[0])
            if keyboard.is_pressed('2'):
                print(f"Closest Color: {color_name}, Distance: {distance}")                
            cv2.putText(image, f"{color_name}", (x2, y1), 0, 1, 0, 3, -1)
            cv2.putText(image, f"{color_nameHSV}", (x2, y1+50), 0, 1, 0, 3, -1)

            # cv2.putText(image, f"Af: {round(r)}, {round(g)}, {round(b)}", (x2, y1+100), 0, 0.5, 0, 2, -1)
            cv2.putText(image, f"Be: {round(r)}, {round(g)}, {round(b)}, + {rDiff}, {gDiff}, {bDiff}", (x2, y1+100), 0, 0.5, 0, 2, -1)
            cv2.putText(image, f"H {round(hue)}, S {round(saturation)}, V {round(value)}", (x2, y1+80), 0, 0.5, 0, 2, -1)

            # cv2.putText(image, f"red: {round(r - smoothed_color_bgr[2])}, green: {round(g - smoothed_color_bgr[1])}, blue: {round(b - smoothed_color_bgr[0])}", (x2, y1+20), 0, 0.5, 0, 2, -1)

            cv2.circle(image, (450, 50), 40, 0, 1)
            cv2.rectangle(image, (x1+10, y1+10), (x2-10, y2-10), (255, 0, 0), 2)
                    # Return processed image (or any other response) to frontend
    _, buffer = cv2.imencode('.jpg', image)
    img_str = base64.b64encode(buffer).decode("utf-8")

    return jsonify({"processed_frame": f"data:image/jpeg;base64,{img_str}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
