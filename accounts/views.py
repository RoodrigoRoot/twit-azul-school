from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from accounts.forms import UserForm, ProfileForm, LoginForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


class RegisterCreateView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = UserForm()
        return render(request, 'users/register.html', locals())

    def post(self, request):
        form = UserForm(request.POST)

        if form.is_valid():

            user = form.save()
            return redirect(reverse('register-profile', kwargs={'pk': user.id}))
        else:
            form = UserForm()
            messages.error(request, 'Please check your data.')

        return render(request, 'users/register.html', locals())


class ProfileRegister(View):

    def get(self, request, pk):
        messages.success(request, 'Now complete this form.')
        form = ProfileForm()
        return render(request, 'users/register.html', locals())

    def post(self, request, pk):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=self.kwargs.get('pk'))
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect(reverse('login'))
        else:
            ...
        return render(request, 'users/register.html', locals())


class LoginView(View):
    template_name = 'users/login.html'

    def get(self, request):
        form = LoginForm()
        messages.success(request, 'Excellent. Please Sing in.')
        return render(request, self.template_name, locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                form = LoginForm()
                messages.error(request, 'Check your credentials.')
        else:
            form = LoginForm()
        return render(request, self.template_name, locals())




