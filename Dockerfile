FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Copy entrypoint script
COPY wait_for_postgres.sh /app/wait_for_postgres.sh
RUN chmod +x /app/wait_for_postgres.sh

EXPOSE 8000

# Use the entrypoint script
CMD ["/app/wait_for_postgres.sh"]

