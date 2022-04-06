import cv2
import numpy as np

def fun(input_data, degree=180):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    degrees = [0,90,180,270,360]
    if(degree not in degrees):
        degree = 180
    if(degree==90):
        rotated_img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    elif(degree==180):
        rotated_img = cv2.rotate(img,cv2.ROTATE_180)
    elif(degree==270):
        rotated_img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
    else:
        rotated_img = img
    return [rotated_img]
