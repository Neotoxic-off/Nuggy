FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["python3", "main.py"]
