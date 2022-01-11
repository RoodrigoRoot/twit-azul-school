from django.shortcuts import render, redirect, reverse
from twit.models import Twit, Comment, Like
from django.views import View
from twit.forms import TwitForm, CommentForm
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


class CommentCreateView(View):

    template_name = 'twits/comments.html'

    def get(self, request, pk):
        twit = Twit.objects.get(pk=pk)
        form = CommentForm()
        return render(request, self.template_name, locals())

    def post(self, request, pk):
        twit = Twit.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                twit=twit,
                author=request.user,
                comment=form.cleaned_data["comment"]
            )
        else:
            form = CommentForm()
        return render(request, self.template_name, locals())


class LikeCreateView(View):

    def post(self, request, pk):
        url_parameter = request.GET.get('url', 'index')
        has_user = request.GET.get('user', False)
        twit = Twit.objects.get(pk=pk)
        like, _ = twit.like_set.get_or_create(author=request.user)
        like.like = not like.like
        like.save()
        if has_user:
            return redirect(reverse(url_parameter, kwargs={'username': request.POST['user']}))
        return redirect(reverse(url_parameter))
