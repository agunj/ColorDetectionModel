import sqlite3
import numpy as np
import cv2

def get_closest_color(r, g, b):
    conn = sqlite3.connect('colors.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, r, g, b FROM Colors")
    colors = cursor.fetchall()

    closest_color_name = None
    closest_color_distance = float('inf')

    for color in colors:
        color_name, db_r, db_g, db_b = color
        distance = np.sqrt((r - db_r) ** 2 + (g - db_g) ** 2 + (b - db_b) ** 2)
        
        if distance < closest_color_distance:
            closest_color_distance = distance
            closest_color_name = color_name

    conn.close()
    return closest_color_name, closest_color_distance

def get_broad_color(h, s, v):
    conn = sqlite3.connect('broad_colors.db')
    cursor = conn.cursor()

    query = """
    SELECT color_name
    FROM broad_colors
    WHERE
        ? BETWEEN min_h AND max_h
        AND ? BETWEEN min_s AND max_s
        AND ? BETWEEN min_v AND max_v
    """
    
    cursor.execute(query, (h, s, v))
    result = cursor.fetchone()
    
    conn.close()
    
    return result[0] if result else "Unknown"

def process_card(image, tl, br, n):
    x1, y1 = tl
    x2, y2 = br
    region = image[y1:y2, x1:x2]

    hsv_image = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)
    
    hsv_pixels = hsv_image.reshape(-1, 3)
    rgb_pixels = region.reshape(-1, 3)

    hsv_sorted = sorted(hsv_pixels, key=lambda x: x[2])
    rgb_sorted = sorted(rgb_pixels, key=lambda x: np.sum(x))

    lowest_hsv = np.mean(hsv_sorted[:n], axis=0)
    highest_rgb = np.mean(rgb_sorted[-n:], axis=0)
    
    lowest_hsv = tuple(map(int, lowest_hsv))
    highest_rgb = tuple(map(int, highest_rgb))
    
    print(f"Lowest HSV (average of bottom {n}): {lowest_hsv}")
    print(f"Highest RGB (average of top {n}): {highest_rgb}")
    
    return lowest_hsv, highest_rgb

if __name__ == "__main__":
    h = 1
    s = 23
    v = 23

    color = get_broad_color(h, s, v)
    print(f"Broad color: {color}")
