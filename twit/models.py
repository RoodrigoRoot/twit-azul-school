from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DatesCreateUpdatedAbstract(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Twit(DatesCreateUpdatedAbstract):

    twit = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.twit}"

    class Meta:
        verbose_name = "Twit"
        verbose_name_plural = "Twits"
        ordering = ["-created_at"]
