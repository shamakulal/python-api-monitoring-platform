FROM python:3.13-slim

WORKDIR /app

COPY health_check.py /app/health_check.py
COPY crontab /etc/cron.d/health-check

RUN apt-get update \
    && apt-get install -y --no-install-recommends cron \
    && chmod 0644 /etc/cron.d/health-check \
    && touch /var/log/health_check.log \
    && rm -rf /var/lib/apt/lists/*

CMD ["cron", "-f"]
