FROM python:3.11-slim

WORKDIR /app

# Install required packages including PostgreSQL client
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
COPY wait_for_postgres.sh /app/wait_for_postgres.sh
RUN chmod +x /app/wait_for_postgres.sh

# Command to run when container starts
# CMD ["gunicorn", "urolog.wsgi:application", "--bind", "0.0.0.0:8000"]
