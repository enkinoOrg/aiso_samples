from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
import cv2
import matplotlib.pyplot as plt

def work_dir():
    return "/".join(__file__.split("/")[:-1])

def anonymize_face_simple(image, factor=3.0):
    (h, w) = image.shape[:2]
    kW = int(w / factor)
    kH = int(h / factor)
    if kW % 2 == 0:
        kW -= 1
    if kH % 2 == 0:
        kH -= 1
    return cv2.GaussianBlur(image, (kW, kH), 0)


def fun(input_data):
    input_data = np.asarray(bytearray(input_data[0].read()))
    img = cv2.imdecode(input_data,cv2.IMREAD_COLOR)

    # 정적파일이 존재하는 경로를 지정
    base_dir = work_dir()
    facenet = cv2.dnn.readNet(f"{base_dir}/deploy.prototxt", f"{base_dir}/res10_300x300_ssd_iter_140000.caffemodel")
    # 얼굴들의 좌표 배열 선언
    faces = list()

    # 입력된 이미지의 높이, 너비 구하기
    h, w = img.shape[:2]

    ## ##
    blob = cv2.dnn.blobFromImage(img, scalefactor=1., size=(300, 300), mean=(104., 177., 123.))
    facenet.setInput(blob)
    dets = facenet.forward()

    ## 순회 하면서 좌표값 추출 ##
    for i in range(dets.shape[2]):
        confidence = dets[0, 0, i, 2]
        if confidence < 0.5:
            continue

        x1 = int(dets[0, 0, i, 3] * w)
        y1 = int(dets[0, 0, i, 4] * h)
        x2 = int(dets[0, 0, i, 5] * w)
        y2 = int(dets[0, 0, i, 6] * h)

        faces.append([x1,x2,y1,y2])

    ## 좌표값의 배열을 순회하면서 사각형 그리기 ##
    for i, xy in enumerate(faces):
        face = img[xy[2]:xy[3], xy[0]:xy[1]]
        face = anonymize_face_simple(face)
        img[xy[2]: xy[3], xy[0]: xy[1]] = face

    return [img]