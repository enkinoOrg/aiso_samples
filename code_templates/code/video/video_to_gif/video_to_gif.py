## video 및 gif 확장자 테스트 중 입니다.
## 이후 아래의 코드가 제대로 작동이 되지 않을 수도 있습니다.

"""
테스트 환경
input video/mp4
output image/gif
gif의 프레임은 15으로 고정되어 있습니다.
"""

import cv2
import numpy as np
import math

def fun(input_data, start_sec=0, end_sec=0):
    # 입력으로 video의 path가 전달됩니다.
    # running_time gif파일의 재싱시간을 설정합니다.

    cap = cv2.VideoCapture(input_data[0])

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if(end_sec == 0):
        end_sec = math.ceil(video_frame / video_fps)
    
    # 웹 페이지에 설정한 에러메시지가 출력됩니다.
    if(start_sec > end_sec):
        raise Exception("end_sec is smaller than start_sec")

    # 프레임 고정
    gif_frame_rate = 15
    fps_ratio = round(video_fps / gif_frame_rate)

    start_frame = round(video_fps * start_sec)
    end_frame = round(video_fps * end_sec) - start_frame

    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    ret = True
    total_frame_cnt = 0
    frames = []
    captured = 0

    dst_width = 640
    dst_height = 480

    while ret:
        ret, frame = cap.read()

        if(np.shape(frame) == ()):
            continue

        if(total_frame_cnt % fps_ratio == 0):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (dst_width, dst_height), cv2.INTER_AREA)
            frames.append(frame)
            captured += 1
        
        if(total_frame_cnt > end_frame):
            break

        total_frame_cnt += 1

    if(cap.isOpened()):
        cap.release()

    return [frames]
