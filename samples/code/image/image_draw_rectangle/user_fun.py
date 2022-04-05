import cv2
import numpy as np
from PIL import Image

def fun(input_data,left_x=250,left_y=250,right_x=500,right_y=500,text="Hello"):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_UNCHANGED)
    rec_img = cv2.rectangle(img, (left_x,left_y), (right_x,right_y), (0, 0, 255), 2, cv2.LINE_8)
    cv2.putText(rec_img,text,(left_x,left_y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 0, 255))
    return [img]
