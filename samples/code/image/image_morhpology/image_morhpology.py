import cv2
import numpy as np

def fun(input_data):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res, img = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
    grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
    return [grad]
