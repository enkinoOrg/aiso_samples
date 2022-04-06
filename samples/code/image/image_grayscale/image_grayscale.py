import cv2
import numpy as np

def fun(input_data):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return [img]
