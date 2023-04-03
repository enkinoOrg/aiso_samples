import cv2
import numpy as np

def fun(input_data,width = 256, height = 256):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    preprocessed_img = cv2.resize(img,dsize=(width,height),interpolation=cv2.INTER_AREA)
    return [preprocessed_img]
