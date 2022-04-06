import cv2
import numpy as np

def fun(input_data,x=5,y=5):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    blured_img = cv2.blur(img,(x,y))
    return [blured_img]
