#!/bin/bash

# wait-for-postgres.sh

set -e

until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  >&2 echo "Waiting for PostgreSQL to start..."
  sleep 1
done

>&2 echo "PostgreSQL is up - executing command"

# Ensure migrations directory exists for account app
mkdir -p /app/account/migrations
touch /app/account/migrations/__init__.py

# Generate migrations for account app if not exists
if [ ! -f /app/account/migrations/0001_initial.py ]; then
  python manage.py makemigrations account
fi

# Run migrations
python manage.py migrate

# Start application
exec python manage.py runserver 0.0.0.0:8000