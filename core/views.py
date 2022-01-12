from django.shortcuts import render, reverse, redirect
from django.views import View
from twit.models import Twit
from accounts.models import Follow
# Create your views here.


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('register'))
        twits = Twit.objects.all()
        return render(request, self.template_name, locals())

