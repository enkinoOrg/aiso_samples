# 기본이미지 로드
FROM python:3.8.13-buster
# 선택적
LABEL maintainer='exmaple@email.com'
# 작업 폴더
WORKDIR /app
# 환경변수 설정
ENV port=3000 host=0.0.0.0
# 포트 노출
EXPOSE ${port}
# 파일 복사
COPY basic.py requirements.txt /app/
# opencv libgl.so.1
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN rm -rf /var/lib/apt/lists/*
# 의존성 설치
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 -m gunicorn -b ${host}:${port} basic:app