#!/bin/bash

until mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" -e "SELECT 1"; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
python manage.py migrate --noinput

echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

exec "$@"
