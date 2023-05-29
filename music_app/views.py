from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, MusicFile
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(email=email, password=password)
        return redirect('login')
    return render(request, 'music_app/register.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request, 'music_app/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def upload_music(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['music_file']
        visibility = request.POST['visibility']
        uploader = request.user
        music_file = MusicFile.objects.create(title=title, file=file, visibility=visibility, uploader=uploader)

        if visibility == MusicFile.PROTECTED:
            allowed_emails = request.POST.getlist('allowed_emails')
            for email in allowed_emails:
                user = User.objects.filter(email=email).first()
                if user is not None:
                    music_file.allowed_emails.add(user)

        return redirect('homepage')

    return render(request, 'music_app/upload_music.html')


@login_required
def homepage(request):
    user = request.user
    music_files = MusicFile.objects.filter(
        Q(visibility=MusicFile.PUBLIC) |
        Q(uploader=user) |
        Q(allowed_emails=user)
    ).distinct()

    context = {
        'music_files': music_files
    }

    return render(request, 'music_app/homepage.html', context)
