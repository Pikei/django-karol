![env_scr](https://github.com/Pikei/django-karol/assets/32680376/0200cb88-9368-4077-b907-9f282873550d)

Użyte komendy w terminalu krok po kroku:

py -m venv karol_env

cd karol_env\Scripts

activate

python -m pip install --upgrade pip 

cd ..

cd ..

pip install -r requirements.txt

django-admin.exe startproject mysite .

python manage.py migrate

python manage.py runserver

python manage.py startapp blog

python manage.py makemigrations blog

python manage.py migrate blog

python manage.py createsuperuser

python manage.py runserver 
