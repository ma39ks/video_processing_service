FROM python:3.8

WORKDIR /app
COPY / /app 

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg

CMD ["python", "main.py"]
