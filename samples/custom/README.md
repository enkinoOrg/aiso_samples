<p align="center">
  <a href="https://aiso.ai/dev/createApp/customApp/customAppCreate/?type=custom">
    <img src="https://user-images.githubusercontent.com/38392519/161871074-38b5cf3e-8a5b-436f-9f10-c6c3943e877c.png" />
  </a>
</p>

# 아이소 커스텀앱 제작 가이드

## 💡 개요
아이소 커스텀앱 제작 가이드입니다.

## ❗ 제한사항
1. 작성 방식
    - 개발자 화면의 커스텀앱 생성을 선택합니다.
    - 왼쪽에 보이는 앱 중 원하는 앱들을 끌어서 우측 만들기 창에 순서대로 놓습니다.
    - 순서대로 정렬된 앱들의 입력과 출력을 설정합니다.
        * 자세한 내용은 아래를 참조하세요.
    - 그 이후에는 기존의 앱들과 같은 방식으로 생성합니다.

2. 가능한 앱들
    - 아이소에 등록한 앱 중에서 library 사용이 허용된 앱들만 사용할 수 있습니다.
    - 커스텀앱을 이용하여 새로운 커스텀앱을 생성하지 못합니다.

3. 입력과 출력
    - 정렬된 앱들의 입력과 출력을 설정할 수 있습니다.
    - 이전 앱의 출력을 현재 앱의 입력순서에 맞추어 설정해주어야 합니다.
        * 1번 앱의 2번째 출력 -> 2번 앱의 1번째 입력
    - 모든 입력과 출력이 연결될 필요는 없습니다.
        * 1번 앱의 출력이 4개, 2번 앱의 입력이 1개여도 실행할 수 있습니다.

4. 앱 삭제와 사용정지
    - 라이브러리로 사용된 앱이 삭제되면 커스텀 앱은 사용이 중지됩니다.
        * 앱 삭제 유예기간 동안은 실행이 가능하며, 남은 일자는 웹사이트에 표시가 됩니다.
    - 앱 삭제 요청 시 유예기간(15일) 후에 이후에 앱이 삭제됩니다.
        * 라이브러리로 사용 중인 앱이 이미 삭제가 되어서 사용정지인 앱은 삭제요청 시 즉시 삭제됩니다.
    - 유예기간이 지나기 전 앱 관리에서 삭제요청을 철회할 수 있습니다.
        * 라이브러리로 사용 중인 앱은 요청 시 바로 삭제가 되므로 철회할 수 없습니다.

