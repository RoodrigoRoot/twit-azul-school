from django import forms


class TwitForm(forms.Form):
    twit = forms.CharField(max_length=60)
