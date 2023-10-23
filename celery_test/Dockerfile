FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip  \
    && pip install --no-cache-dir -r ./requirements.txt

COPY . .

#CMD ["python", "conecter.py"]

#CMD ["celery", "-A", "tasks", "worker","--loglevel=INFO"]

#CMD ["python", "executer_tasks.py"]

