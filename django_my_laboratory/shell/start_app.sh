#!/bin/bash
poetry run python ../manage.py makemigrations
poetry run python ../manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | poetry run python ../manage.py shell