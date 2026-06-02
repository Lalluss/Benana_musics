FROM python:3.10.8-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git ffmpeg -y

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install --ignore-installed --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
