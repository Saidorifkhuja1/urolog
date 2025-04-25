#!/bin/bash
# wait-for-postgres.sh

set -e

host="$DB_HOST"
port="$DB_PORT"
user="$DB_USER"
password="$DB_PASSWORD"
db="$DB_NAME"

echo "Waiting for PostgreSQL to start..."

# Try with nc first (doesn't require psql)
until nc -z "$host" "$port"; do
  echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

# Then check if we can connect with psql
until PGPASSWORD=$password psql -h "$host" -U "$user" -d "$db" -c '\q' 2>/dev/null; do
  echo "PostgreSQL is accepting connections but not ready for queries - sleeping"
  sleep 1
done

echo "PostgreSQL is up - executing command"