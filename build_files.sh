#!/bin/bash
# Set Django settings module
export DJANGO_SETTINGS_MODULE=myabb.settings

# Install dependencies
pip install -r requirements.txt

# Create staticfiles directory if not exist
mkdir -p staticfiles_build/static

# Collect static files
python manage.py collectstatic --noinput --clear
