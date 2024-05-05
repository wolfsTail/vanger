# Проект Django с использованием Docker

## Описание
Этот проект разработан на Django 4.1 и Python 3.9, использует MySQL в качестве базы данных. Клиентская часть реализована с помощью Bootstrap 5. Особенностью проекта является использование slick slider для отображения слайдера на главной странице, а также возможность управления содержимым слайдера через админ-панель Django.

## Функциональные возможности
- **Slick Slider**: Используется для создания интерактивного слайдера на главной странице.
- **Просмотр в полном экране**: По клику на изображение в слайдере открывается полноэкранная галерея.
- **Управление содержимым слайдера через админку**: Интерфейс администратора позволяет управлять слайдами, загружать изображения через django-filer и сортировать их с помощью drag&drop.

## Стэк
- Docker
- Python 3.9
- Django 4.1
- MySQL
- Bootstrap 5
- Slick Slider

## Порядок использования

### Клонирование репозитория
Склонируйте репозиторий на ваш локальный компьютер с помощью следующей команды:
```bash
git clone https://github.com/wolfsTail/vanger.git
cd vanger
```

### Запуск проекта
Запустите сборку контейнеров и запуск проекта
```bash
docker-compose up --build
```

### Инициализация проекта
Выполните миграции и создайте суперпользователя
```bash
docker-compose exec web-app python manage.py migrate
docker-compose exec web-app python manage.py createsuperuser
```

### Доступ к проекту
После запуска и инициализации проекта, он будет доступен по [адресу](http://localhost:8000).
Используйте зарегистрированные Вами ранне данные суперпользователя для доступа к [админ-панели](http://localhost:8000/admin).

### Загрузка изображений
В админ-панели перейдите во вкладку __"Папки"__ раздела __"FILER"__.Создайте новую папку и загрузите в неё интересущие Вас изображения.

### Создание слайдов
В админ-панели перейдите во вкладку __"Слайды"__ раздела __"Слайдер"__. Нажмите __"Добавить слайд"__, придумайте название слайда и выбери изображении из ранее загруженных. Нажмите __"Cохранить"__.

### Заключение
Наслаждайтесь видом своих изображений ([ссылка](http://localhost:8000))!