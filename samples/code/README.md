# 아이소에 코드앱 샘플 디렉토리

## 💡 개요
아이소 코드 앱 작성 가이드 및 샘플코드입니다.

## 제한사항
1. 입력 값.
    - 앱 실행시 입력한 데이터는 input_data 변수에 담겨져 전달됩니다.
    - input_data의 데이터 형식은 List[ bytes buffer | string ]
    - 입력 데이터의 순서는 앱 생성시 정해진 순서대로 정해집니다.
    ```
    def fun(input_data):
        img_bytes = input_data[0]
        string_data = input_data[1]
        ...
    ```
2. 파라미터.
    - 앱 실행시마다 변경이 가능한 변수를 파라미터로 지정할 수 있습니다.
    - 도입함수(fun)의 파라미터로 값으로 넣으면 됩니다.
    ```
    def fun(input_data, size=12, flag=True):
        ...
    ```
3. 제한사항.
    - 이름 규칙
        1. 도입 함수
            - 도입 함수의 이름은 항상 fun이여야 하며, 다른 함수로 덮어씌우거나, 해당 함수가 존재지 않을시 에러가 발생합니다.
        2. 입력데이터
            - 입력 데이터 변수의 이름은 항상 input_data입니다.
    - 출력 규칙
        1. 출력의 개수는 앱 생성시 설정한 개수 만큼 반환되어야 합니다.
        2. 출력데이터의 순서는 앱 생성시 설정한 순서대로 반환되어야 합니다.
        3. image 데이터는 numpy.ndarray형태로, text 데이터는 string형태로 반환되어야 합니다.

- [License](#-license)
## 📝 License
Licensed under the [MIT License](./LICENSE).