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
    - 앱 실행시 입력한 데이터는 input_data 변수에 담겨져 전달됩니다.
    - input_data의 데이터 형식은 List[ bytes buffer | string ]
    - 입력 데이터의 순서는 앱 생성시 정해진 순서대로 정해집니다.
    ```
    def fun(input_data):
        img_bytes = input_data[0]
        string_data = input_data[1]
        ...
    ```

2. 파라미터
    - 앱 실행시마다 변경이 가능한 변수를 파라미터로 지정할 수 있습니다.
    - 도입함수(fun)의 파라미터로 값으로 넣으면 됩니다.
    ```
    def fun(input_data, size=12, flag=True):
        ...
    ```

3. 정적파일 업로드
    - 설정파일, 모델과 같은 정적파일을 앱 생성시 같이 업로드하여 앱 생성이 가능합니다.
    - 해당 정적파일들은 앱이 실행되는 위치에 같이 놓이게 됩니다.

4. 제한사항
    - 이름 규칙
        * 도입 함수
            - 도입 함수의 이름은 항상 fun이여야 하며, 다른 함수로 덮어씌우거나, 해당 함수가 존재지 않을시 에러가 발생합니다.
        * 입력 데이터
            - 입력 데이터 변수의 이름은 항상 input_data 입니다.
    - 출력 규칙
        * 출력의 개수는 앱 생성시 설정한 개수 만큼 반환되어야 합니다.
        * 출력데이터의 순서는 앱 생성시 설정한 순서대로 반환되어야 합니다.
        * image 데이터는 numpy.ndarray형태로, text 데이터는 string형태로 반환되어야 합니다.
    - 모듈 제한
        * 실행시 실행환경을 변경이 가능한 모듈은 로드하지 못합니다.
        * 아래의 모듈은 사용하지 못합니다.
            ```
            "os", "sys", "subprocess", "importlib", "posix", "pathlib",
            "shutil", "glob", "tempfile", "fileinput", "filecmp", "linecache", 
            "urllib", "http", "requests"
            ```
5. 앱 삭제
    - 앱 삭제 요청시 유예기간(15일) 후에 이후에 앱이 삭제가 됩니다.
        * 만약 앱이 커스텀앱의 라이브러리로 사용중이라면 해당 커스텀 앱은 유예기간이 지난 후에 사용이 중지됩니다.
    - 유예기간이 지나기 전 앱 관리에서 삭제요청을 철회할 수 있습니다.

6. 실행환경
    * Python Version: Python3.8
    * 메모리: 1GB
    * 실행시간 제한: 180초
    * 의존성: [requirements.txt](https://github.com/enkinoOrg/aiso_samples/tree/main/samples/code/requirements.txt)
