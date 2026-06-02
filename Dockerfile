FROM python:3.10.8-slim-buster

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends git ffmpeg imagemagick && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --ignore-installed -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
