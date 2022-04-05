import cv2
import numpy as np

def fun(input_data,kernel_size=5,sigma=3):
    img_bytes = input_data[0]
    input_data = np.asarray(bytearray(img_bytes.read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)
    kernel1d = cv2.getGaussianKernel(kernel_size,sigma)
    kernel2d = np.outer(kernel1d,kernel1d.transpose())
    low = cv2.filter2D(img,-1,kernel2d)
    high = img - low + 128
    return [high]
