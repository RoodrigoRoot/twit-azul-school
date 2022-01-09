from django.shortcuts import render, reverse, redirect
from django.views import View
# Create your views here.


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect(reverse('register'))
        return render(request, self.template_name, locals())

