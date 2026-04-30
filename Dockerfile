FROM python:3.10-slim

WORKDIR /app
COPY /app .

RUN pip install flask prometheus_client

CMD ["python", "app.py"]