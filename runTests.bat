docker-compose.exe run web sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py test"
PAUSE