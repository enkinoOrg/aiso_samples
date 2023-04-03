<p align="center">
  <a href="https://aiso.ai/dev/createApp/codeApp/codeAppCreate/?type=code">
    <img src="https://user-images.githubusercontent.com/38392519/161871092-dd937c1d-953e-4bd4-ba9d-92a97fb648e0.png" />
  </a>
</p>

# 아이소 코드앱 제작 가이드

## 💡 개요
아이소 코드 앱 작성 가이드 및 샘플코드입니다.

## ❗ 제한사항
1. 입력 값
    - 앱 실행 시 입력한 데이터는 input_data 변수에 담겨 전달됩니다.
    - input_data의 데이터 형식은 배열 데이터 타입입니다.
        - 이미지의 경우 배열의 인자들이 bytes buffer으로 전달됩니다.
        - text데이터의 경우 배열의 인자들이 str으로 전달됩니다.
    - 입력 데이터의 순서는 앱 생성 시 정해진 순서대로 정해집니다.
    ```
    def fun(input_data):
        img_bytes = input_data[0]
        string_data = input_data[1]
        ...
    ```

2. 반환 값
    - 반환 값의 형태는 배열이어야 합니다.
    - 앱 생성 시 설정한 출력의 개수와 반환 값의 길이가 같아야 합니다.
    - 반환 값의 순서는 앱 생성 시 설정한 순서대로 설정되어야 합니다.
    - image 데이터는 numpy.ndarray, text 데이터는 str 형태로 반환되어야 합니다.
    ```
    def fun(input_data):
        ...
        return [numpy.ndarray, str ...]
    ```

3. 파라미터
    - 앱 실행 시마다 변경이 가능한 변수를 파라미터로 지정할 수 있습니다.
    - 도입함수(fun)의 파라미터로 값으로 넣으면 됩니다.
        - input_data 뒤에 차례로 넣으면 됩니다.
    ```
    def fun(input_data, size=12, flag=True):
        ...
    ```

4. 정적파일 업로드
    - 설정 파일, 모델과 같은 정적파일을 앱 생성 시 같이 업로드하여 앱 생성이 가능합니다.
    - 해당 정적파일들은 앱이 실행되는 위치에 같이 놓이게 됩니다.

5. 정적파일 불러오기
    - 모듈 제한정책으로 인하여 앱 생성 시 업로드한 정적파일을 불러올 때 경로를 지정하는데 os, pathlib을 사용하지 못합니다.
    - 정적파일을 불러오거나 파일이 있는 위치를 가져올 때 아래의 함수를 넣어서 경로를 얻으실 수 있습니다.
        ```
        def work_dir():
            return "/".join(__file__.split("/")[:-1])
        ```

6. 제한사항
    - 이름 규칙
        * 도입 함수
            - 도입 함수의 이름은 항상 fun이여야 합니다.
                - 도입 함수가 없거나 포맷이 변경될 경우 에러가 발생합니다.
        * 입력 데이터
            - 입력 데이터 변수의 이름은 항상 input_data입니다.
    - 모듈 제한
        * 실행 시 실행환경을 변경이 가능한 모듈은 로드하지 못합니다.
        * 아래의 모듈은 사용하지 못합니다.
            ```
            "os", "sys", "subprocess", "importlib", "posix", "pathlib",
            "shutil", "glob", "tempfile", "fileinput", "filecmp", "linecache", 
            "urllib", "http", "requests"
            ```

7. 앱 삭제
    - 앱 삭제 요청 시 유예기간(15일) 후에 이후에 앱이 삭제됩니다.
        * 만약 앱이 커스텀앱의 라이브러리로 사용 중이라면 해당 커스텀 앱은 유예기간이 지난 후에 사용이 중지됩니다.
    - 유예기간이 지나기 전 앱 관리에서 삭제요청을 철회할 수 있습니다.

8. 실행환경
    * Python 버전: Python3.8
    * 메모리: 1GB
    * 실행시간 제한: 180초
    * 의존성: [requirements.txt](https://github.com/enkinoOrg/aiso_samples/tree/main/samples/code/requirements.txt)
