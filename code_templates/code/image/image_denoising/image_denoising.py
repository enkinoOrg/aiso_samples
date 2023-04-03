import cv2
import numpy as np

def fun(input_data):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
    return [dst]
