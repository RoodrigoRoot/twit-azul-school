from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DatesCreateUpdatedAbstract(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Twit(DatesCreateUpdatedAbstract):

    twit = models.CharField(max_length=60)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.twit}"

    class Meta:
        verbose_name = "Twit"
        verbose_name_plural = "Twits"


class Comment(DatesCreateUpdatedAbstract):

    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.twit}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Like(DatesCreateUpdatedAbstract):

    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.author.username

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
