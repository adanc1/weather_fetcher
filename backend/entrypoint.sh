#!/bin/sh

echo "Waiting for PostgreSQL..."

while ! nc -z etl-postgres 5432; do
  sleep 1
done

echo "PostgreSQL started"

exec uvicorn main:app --host 0.0.0.0 --port 8000
