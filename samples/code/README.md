# 아이소에 코드앱 샘플 디렉토리

## 💡 개요
아이소 코드 앱 작성 가이드 및 샘플코드입니다.

## 제한사항
1. 파라미터.
    - 아이소에서 서버로 요청을 보낼때 POST로 요청을 보냅니다.
2. 입력 값.
    - 헤더는 URL앱 작성시 설정이 가능합니다.
    - 인증 및 데이터 적재를 위하여 설정이 가능합니다.
3. 출력 값 제한사항.
    - 필수 데이터
        1. input_url
            - input_url은 List[str] 형태로 전달됩니다.
            - 해당 값은 모두 singed url으로써 입력 파일을 바로 다운이 가능합니다.
            - 길이는 앱 실행시 입력한 파일의 개수입니다.
        2. header
            - header는 위의 request header와 다르게 body안의 값입니다.
            - header은 List[Dict[str,str]] 형태로 전달됩니다.
            - 결과를 업로드 요청을 할때 같이 보내지는 값입니다.
        3. upload_url
            - upload_url은 List[str] 형태로 전달됩니다.
            - 실행결과를 응답에 답아서 반환하지 않으며 해당 url로 업로드합니다.

    - 옵션
        1. 파라미터
            - 앱 생성시 실행때마다 값을 변경할 수 있는 파라미터를 설정할 수 있습니다.
            - 데이터 타입은 int, float, string, bool 형식이 가능합니다.
            - 여러개의 파라미터를 가질 수 있습니다.
            - 전달되는 방식은 body값에 담겨져 전달되며 생성시 설정한 이름의 KEY값으로 전달됩니다.
                * 예시: 파라미터 size를 설정시, { input_url: ..., header: ..., upload_url: ..., size: ...}
- [License](#-license)
## 📝 License
Licensed under the [MIT License](./LICENSE).