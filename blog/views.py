from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def signUp(request):
    User = get_user_model()
    if request.user.is_authenticated:
        return render(request=request, template_name="home.html")

    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password1', '')
        dob = request.POST.get('dob', '')
        gender = request.POST.get('gender', '')
        user = User.objects.create_user(username = username, email = email,
                                        password = password, dob = dob, gender = gender)

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect("/home")

    return render(request=request, template_name="blog/signUp.html", context={})


def signIn(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/post_list")
        else:
            return HttpResponse("fail")

    return render(request=request, template_name="blog/signIn.html", context={})


def home(request):
    return render(request=request, template_name="blog/post_list.html", contex={})


def signOut(request):
    return render(request=request, template_name="blog/post_list.html", context={})
