from django.contrib import admin
from twit.models import Twit, Comment, Like
# Register your models here.

admin.site.register(Twit)
admin.site.register(Comment)
admin.site.register(Like)
