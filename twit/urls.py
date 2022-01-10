from django.urls import path
from twit.views import CreateTwit

app_name = "twit"

urlpatterns = [
    path('add/', CreateTwit.as_view(), name="create-twit"),
]


