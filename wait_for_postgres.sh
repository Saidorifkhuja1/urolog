#!/bin/bash
# wait-for-postgres.sh

set -e

host="$DB_HOST"
user="$DB_USER"
password="$DB_PASSWORD"
db="$DB_NAME"

echo "Waiting for PostgreSQL to start..."

until PGPASSWORD=$password psql -h "$host" -U "$user" -d "$db" -c '\q'; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

echo "PostgreSQL is up - executing command"