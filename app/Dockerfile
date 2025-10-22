FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

RUN apt-get update && apt-get install -y cron && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "0 * * * * /usr/local/bin/python3 /app/main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/hourly-job \
    && chmod 0644 /etc/cron.d/hourly-job \
    && crontab /etc/cron.d/hourly-job

CMD ["cron", "-f"]
