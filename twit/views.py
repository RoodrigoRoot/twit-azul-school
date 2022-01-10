from django.shortcuts import render, redirect, reverse, resolve_url
from twit.models import Twit
from django.views import View
from twit.forms import TwitForm
from django.http.response import JsonResponse
# Create your views here.


class CreateTwit(View):

    def post(self, request):
        url_parameter = request.GET.get('url', 'index')
        has_user = request.GET.get('user', False)
        form = TwitForm(request.POST)
        if form.is_valid():
            Twit.objects.create(
                twit=form.cleaned_data["twit"],
                author=request.user
            )
            if has_user:
                return redirect(reverse(url_parameter, kwargs={'username': request.user.username}))
            else:
                return redirect(reverse(url_parameter))
        else:
            return JsonResponse({'error': 'KO'})




