from django import forms
from django.forms import Form


class UserPost(Form):
    author = forms.CharField(max_length=50, min_length=6, error_messages={'min_length': '用户名长度至少6位'})
    content = forms.CharField(max_length=140)
