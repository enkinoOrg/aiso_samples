<p align="center">
  <a href="https://aiso.ai/dev/createApp/urlApp/urlAppCreate/?type=url">
    <img src="https://user-images.githubusercontent.com/38392519/161871044-f6d20d71-9559-407f-aa4a-1df3e175909a.png" />
  </a>
</p>

# 아이소 URL앱 샘플 디렉토리

## 💡 개요
아이소에 등록이 가능하도록 작성한 서버 작성 가이드 및 샘플코드입니다.

## ❗ 제한사항

1. 요청 메서드
    - 아이소에서 서버로 요청을 보낼 때 POST로 요청을 보냅니다.

2. 요청 헤더
    - 헤더는 URL앱 작성 시 설정이 가능합니다.
    - 인증 및 데이터 적재를 위하여 설정할 수 있습니다.

3. 요청 메시지
    - 필수 데이터
        * input_url
            - input_URL은 List[str] 형태로 전달됩니다.
            - 해당 값은 모두 singed url로서 입력 파일을 바로 다운할 수 있습니다.
            - 길이는 앱 실행 시 입력한 파일의 개수입니다.
        * header
            - header는 위의 request header와 다르게 body 안의 값입니다.
            - header는 List[Dict[str, str]] 형태로 전달됩니다.
            - 결과를 업로드 요청을 할 때 같이 보내지는 값입니다.
        * upload_url
            - upload_url은 List[str] 형태로 전달됩니다.
            - 실행 결과를 응답에 담아서 반환하지 않으며 해당 URL로 업로드합니다.

    - 옵션
        * 파라미터
            - 앱 생성 시 실행 때마다 값을 변경할 수 있는 파라미터를 설정할 수 있습니다.
            - 데이터 타입은 int, float, string, bool 형식이 가능합니다.
            - 여러 개의 파라미터를 가질 수 있습니다.
            - 전달되는 방식은 body 값에 담겨 전달되며 생성 시 설정한 이름의 KEY 값으로 전달됩니다.
                * 예시: 파라미터 size를 설정 시, { input_url: ..., header: ..., upload_url: ..., KEY: ...}

4. 응답
    - 실행 결과 자체를 반환받지 않으며, 상태코드(status code)를 바탕으로 실행 결과를 판단합니다.
    - 상태코드가 200이 아닐 경우 에러로 처리합니다.

5. 앱 삭제
    - 앱 삭제 요청 시 유예기간(15일) 후에 이후에 앱이 삭제됩니다.
        * 만약 앱이 커스텀앱의 라이브러리로 사용 중이라면 해당 커스텀 앱은 유예기간이 지난 후에 사용이 중지됩니다.
    - 유예기간이 지나기 전 앱 관리에서 삭제요청을 철회할 수 있습니다.

6. 예제코드
    - 위의 설명을 바탕으로 작성한 예제코드입니다.
    - 하위 폴더 예제들의 의존성 목록은 [requirements.txt](https://github.com/enkinoOrg/aiso_samples/tree/main/samples/url/requirements.txt) 입니다.
    ```
    try:
        ## 메시지 파싱 ##
        recevied_msg = json.loads(request.get_data().decode("utf-8"))
        input_urls = recevied_msg["input_url"]
        style = recevied_msg["style"]
        headers = recevied_msg["header"]
        upload_urls = recevied_msg["upload_url"]

        img_url = input_urls[0]
        header = headers[0]
        upload_url = upload_urls[0]

        # 모델 로드
        model = load_model(style)

        # url로 이미지 요청
        res = requests.get(img_url)

        ## 이미지 읽기 ##
        data = io.BytesIO(res.content)
        pil_img = Image.open(data)
        img = load_img(pil_img)

        # 예측
        pred = prediction(img, model)

        # cv2로 출력가능하게 변환
        pred = convert_cv2(pred)

        ## 처리 후 업로드 ##
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, encimg = cv2.imencode('.jpg', pred, encode_param)
        img_bytes = io.BytesIO(encimg)
        res = requests.put(upload_url, data=img_bytes, headers=header)

        # 응답
        return Response(response=res.content.decode("utf-8"), status=res.​​status_code)
    except Exception:
        error = traceback.format_exc()
        return Response(response=error, status=400)
    ```
