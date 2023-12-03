FROM python:3.10-slim-buster
LABEL authors="lyapin"

WORKDIR /app


COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD ["python3", "mongo_up.py"]