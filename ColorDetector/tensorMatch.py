import cv2
import torch
import torchvision.transforms as transforms
import numpy as np

template_path = 'color_correction_card.png'
template = cv2.imread(template_path, cv2.IMREAD_COLOR)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template_tensor = transforms.ToTensor()(template_gray).unsqueeze(0)

def match(frame, template_tensor, scales=[0.25, 0.5, 0.75, 1.0, 1.25, 1.5], threshold=0.8):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_tensor = transforms.ToTensor()(frame_gray).unsqueeze(0)

    frame_np = frame_tensor.squeeze().numpy()
    template_np = template_tensor.squeeze().numpy()

    for scale in scales:
        # Resize template based on the current scale
        scaled_template = cv2.resize(template_np, (0, 0), fx=scale, fy=scale)
        
        # Check if scaled template is smaller than the frame
        if scaled_template.shape[0] > frame_np.shape[0] or scaled_template.shape[1] > frame_np.shape[1]:
            continue  # Skip this scale if template is larger
        
        res = cv2.matchTemplate(frame_np, scaled_template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val >= threshold:
            top_left = max_loc
            bottom_right = (top_left[0] + scaled_template.shape[1], top_left[1] + scaled_template.shape[0])
            return top_left, bottom_right

    return (0,0), (0,0)