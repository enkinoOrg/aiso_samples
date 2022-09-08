## video 테스트 중 입니다.
## 이후 아래의 코드가 제대로 작동이 되지 않을 수도 있습니다.

import cv2
import numpy as np

def fun(input_data):
    input_video_path = input_data[0]
    cap = cv2.VideoCapture(input_video_path)

    dst_width = 640
    dst_height = 480

    frames = []
    ret = True

    while ret:
        ret, frame = cap.read()
        if(np.shape(frame) == ()):
            continue
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized_frame = cv2.resize(gray_frame, (dst_width, dst_height), cv2.INTER_AREA)
        frames.append(resized_frame)

    if(cap.isOpened()):
        cap.release()

    return [frames]