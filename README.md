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

PYTHON ANYWHERE:

pip3.6 install --user pythonanywhere

pa_autoconfigure_django.py https://github.com/Pikei/django-karol.git

cd pikej.pythonanywhere.com

git pull

LOCAL:

python manage.py shell

DJANGO CONSOLE:

Post.objects.all()

from blog.models import Post

Post.objects.all()

Post.objects.create(author=me, title='Sample title', text='Test')

from django.contrib.auth.models import User

User.objects.all()

me = User.objects.get(username='Piotr')

Post.objects.create(author=me, title='Sample title', text='Test')

Post.objects.all()

Post.objects.filter(author=me)

from django.utils import timezone

Post.objects.filter(published_date__lte=timezone.now())

post = Post.objects.get(title="Sample title")

post.publish()

Post.objects.filter(published_date__lte=timezone.now())

Post.objects.order_by('created_date')

Post.objects.order_by('-created_date')

Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

exit()

PYTHON ANYWHERE:

workon pikej.pythonanywhere.com

python manage.py collectstatic

