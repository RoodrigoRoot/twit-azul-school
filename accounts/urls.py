from django.urls import path
from accounts.views import (RegisterCreateView, LoginView,
                            ProfileRegister)


urlpatterns = [
    path('register/', RegisterCreateView.as_view(), name='register'),
    path('register/profile/<int:pk>/', ProfileRegister.as_view(), name='register-profile'),
    path('login/', LoginView.as_view(), name='login'),
]

