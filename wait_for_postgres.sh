#!/bin/sh

# Wait until PostgreSQL is ready
echo "Waiting for PostgreSQL..."

while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL started"

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application
exec gunicorn core.wsgi:application --bind 0.0.0.0:8000


