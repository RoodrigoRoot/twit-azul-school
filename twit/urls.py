from django.urls import path
from twit.views import CreateTwit, CommentCreateView, LikeCreateView

app_name = "twit"

urlpatterns = [
    path('add/', CreateTwit.as_view(), name="create-twit"),
    path('<int:pk>/comment/add/', CommentCreateView.as_view(), name="comment"),
    path('<int:pk>/like/add/', LikeCreateView.as_view(), name="like"),
]


