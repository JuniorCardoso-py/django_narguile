# django_narguile


TO RUN

In your terminal

source .env.development

docker run -e POSTGRES_PASSWORD=olist123 -e POSTGRES_USER=olist -e POSTGRES_DB=olist -p 5433:5432 -d postgres

python manage.py runserver