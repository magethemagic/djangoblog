from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form

from apps.user.models import UserProfile


class UserRegisterForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'phone_number', 'email', 'password']


class UserLoginForm(Form):
    username = forms.CharField(max_length=50, min_length=6, error_messages={'min_length': '用户名长度至少6位'})
    password = forms.CharField(required=True, error_messages={'required': '必须填写密码'},
                               widget=forms.widgets.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not UserProfile.objects.filter(username=username).exists():
            raise ValidationError('用户名不存在')
        return username
