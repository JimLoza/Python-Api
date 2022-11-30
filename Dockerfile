FROM python:3.9-alpine

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip 

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "src/app.py"]