FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . .

RUN apt-get update && apt-get install -y cron && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo '#!/bin/bash\n\
printenv | grep -v "no_proxy" >> /etc/environment\n\
echo "* * * * * /usr/local/bin/python3 /app/main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/hourly-job\n\
chmod 0644 /etc/cron.d/hourly-job\n\
crontab /etc/cron.d/hourly-job\n\
cron -f' > /entrypoint.sh && chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
