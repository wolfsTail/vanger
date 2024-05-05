#!/bin/bash
# Ожидание полной готовности MySQL
until mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASSWORD" -e "SELECT 1"; do
  >&2 echo "MySQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "MySQL is up - executing command"
# Выполнение миграций
python manage.py migrate --noinput

# Создание суперпользователя через Django shell
echo "from users.models import CustomUser; CustomUser.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

# Запуск сервера
exec "$@"
