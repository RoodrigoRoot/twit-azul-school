from django import forms


class TwitForm(forms.Form):
    twit = forms.CharField(max_length=60, required=True)


class CommentForm(forms.Form):

    comment = forms.CharField(max_length=150, required=True)


