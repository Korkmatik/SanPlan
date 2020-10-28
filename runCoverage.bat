docker-compose.exe run web sh -c "python manage.py makemigrations && python manage.py migrate && coverage erase && coverage run manage.py test && coverage report"
