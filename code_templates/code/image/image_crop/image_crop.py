import cv2
import numpy as np

def fun(input_data, width=150, height=150):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    x = img.shape[0]
    y = img.shape[1]
    x_center = x/2
    y_center = y/2
    new_x = x_center - width/2
    new_y = y_center - height/2
    cropped_img = img[int(new_y):int(new_y+height), int(new_x):int(new_x+width)]
    return [cropped_img]

