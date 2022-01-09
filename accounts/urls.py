from django.urls import path
from accounts.views import (RegisterCreateView, LoginView,
                            ProfileRegister, ProfileGetUpdateView)


urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('register/profile/<int:pk>/', ProfileRegister.as_view(), name='register-profile'),
    path('login/', LoginView.as_view(), name='login'),

    path('<str:username>/', ProfileGetUpdateView.as_view(), name='profile'),
]

