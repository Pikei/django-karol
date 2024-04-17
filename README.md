![env_scr](https://github.com/Pikei/django-karol/assets/32680376/0200cb88-9368-4077-b907-9f282873550d)

# Commands:
## Local:
1. py -m venv karol_env
2. cd karol_env\Scripts
3. activate
4. python -m pip install --upgrade pip
5. cd ..
6. cd ..
7. pip install -r requirements.txt
8. django-admin.exe startproject mysite .
9. python manage.py migrate
10. python manage.py runserver
11. python manage.py startapp blog
12. python manage.py makemigrations blog
13. python manage.py migrate blog
14. python manage.py createsuperuser
15. python manage.py runserver 

## Python anywhere:
1. pip3.6 install --user pythonanywhere
2. pa_autoconfigure_django.py https://github.com/Pikei/django-karol.git
3. cd pikej.pythonanywhere.com
4. git pull

## Local:
1. python manage.py shell

## Django console:
1. Post.objects.all()
2. from blog.models import Post
3. Post.objects.all()
4. Post.objects.create(author=me, title='Sample title', text='Test')
5. from django.contrib.auth.models import User
6. User.objects.all()
7. me = User.objects.get(username='Piotr')
8. Post.objects.create(author=me, title='Sample title', text='Test')
9. Post.objects.all()
10. Post.objects.filter(author=me)
11. from django.utils import timezone
12. Post.objects.filter(published_date__lte=timezone.now())
13. post = Post.objects.get(title="Sample title")
14. post.publish()
15. Post.objects.filter(published_date__lte=timezone.now())
16. Post.objects.order_by('created_date')
17. Post.objects.order_by('-created_date')
18. Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
19. post = Post.objects.all()
20. post[0].publish()
21. exit()

## Python anywhere:
1. workon pikej.pythonanywhere.com
2. python manage.py collectstatic

## Local:
1. pip install psycopg2
2. python manage.py makemigrations 
3. python manage.py migrate
4. python manage.py createsuperuser 
5. python manage.py runserver