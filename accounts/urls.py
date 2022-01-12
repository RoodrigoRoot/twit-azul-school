from django.urls import path
from accounts.views import (RegisterCreateView, LoginView,
                            ProfileRegister, ProfileGetUpdateView,
                            FollowCreateView)


urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('register/profile/<int:pk>/', ProfileRegister.as_view(), name='register-profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('follows/', FollowCreateView.as_view(), name='following'),
    path('<str:username>/', ProfileGetUpdateView.as_view(), name='profile'),


]

