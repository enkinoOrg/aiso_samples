from flask import Flask, Response, request
import cv2
import io
import numpy as np
import requests
import json

app = Flask(__name__)


def task(image: np.ndarray,) -> np.ndarray:
    return image

def auth(Authorization: str) -> bool:
    # 인증과정
    auth_result = ...
    return auth_result

@app.route("/")
def index():
    # aiso에서는 POST요청이외에는 보내지 않음
    if(request.method != "POST"):
        return Response(response="Method Not Allowed", status=405)

    # request parsing
    # POST BODY WITH Header
    #
    # {
    #     "input_url": List[str],            # 입력으로 넣은 데이터의 signed url
    #     "header": List[Dict[str,str]],     # 결과 데이터의 Content-Type
    #     "upload_url": List[str]            # 결과 데이터의 업로드 singed url
    # }

    aiso_request = json.loads(request.get_data().decode("utf-8"))

    # 필수(required)
    img_url = aiso_request["input_url"][0]
    header = aiso_request["header"][0]
    upload_url = aiso_request["upload_url"][0]
    # Header(optional)
    jwt = aiso_request.headers["Authorization"]
    if(auth(jwt)):
        return Response(response="auth fail", status=401)

    # url로 이미지 요청, img
    res = requests.get(img_url)

    # 이미지 읽기
    data = io.BytesIO(res.content)
    input_data = np.asarray(bytearray(data.read()))
    cv2_img = cv2.imdecode(input_data, cv2.IMREAD_COLOR)

    # task 실행(resize)
    result_img = task(cv2_img)

    # 결과 전 치리 
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, encimg = cv2.imencode('.jpg', result_img, encode_param)
    img_bytes = io.BytesIO(encimg)

    # 결과 업로드
    # singed url을 통해 결과 업로드
    res = requests.put(upload_url, data=img_bytes, headers=header)

    # 결과 상태 보고
    # 상태 200번 이외에는 에러가 발생으로 간주
    return Response(response="ok", status=200)
