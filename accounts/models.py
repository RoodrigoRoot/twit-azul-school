from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()
    location = models.CharField(max_length=150)
    website = models.URLField()
    date_birth = models.DateField()
    profile_picture = models.ImageField(null=True, blank=True)
    background_picture = models.ImageField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

