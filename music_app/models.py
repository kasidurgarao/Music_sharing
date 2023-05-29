from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)


class MusicFile(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    PROTECTED = 'protected'
    VISIBILITY_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (PROTECTED, 'Protected'),
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    allowed_emails = models.ManyToManyField(User, related_name='allowed_music_files', blank=True)



