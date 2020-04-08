from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from apps.article.models import Article
from apps.user.forms import UserRegisterForm, UserLoginForm
from apps.user.models import UserProfile


def index(request):
    articles = Article.objects.all().order_by('-created_date')
    return render(request, 'index.html', context={'articles': articles})


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user/sign-up.html')
    else:
        rform = UserRegisterForm(request.POST)
        if rform.is_valid():
            username = rform.cleaned_data.get('username')
            email = rform.cleaned_data.get('email')
            phone_number = rform.cleaned_data.get('phone_number')
            password = rform.cleaned_data.get('password')
            if not UserProfile.objects.filter(
                    Q(username=username) | Q(email=email) | Q(phone_number=phone_number)).exists():
                password = make_password(password)
                user = UserProfile.objects.create(username=username, phone_number=phone_number, email=email,
                                                  password=password)
                if user:
                    return render(request, 'user/sign-in.html', context={'msg': '注册成功，请登录'})
            else:
                return render(request, 'user/sign-up.html', context={'msg': '用户已存在'})
        return render(request, 'user/sign-up.html', context={'msg': '用户注册失败'})


def user_login(request):
    if request.method == 'GET':
        return render(request, 'user/sign-in.html')
    else:
        lform = UserLoginForm(request.POST)
        if lform.is_valid():
            username = lform.cleaned_data.get('username')
            password = lform.cleaned_data.get('password')
            user = UserProfile.objects.filter(username=username).first()
            flag = check_password(password, user.password)
            # print(flag)
            if flag:
                request.session['username'] = username
                request.session['user_avatar'] = user.user_avatar
                request.session['desc'] = user.user_desc
                return redirect(reverse('index'))
            else:
                msg = '密码错误'
                return render(request, 'user/sign-in.html', context={'msg': msg})
        return render(request, 'user/sign-in.html', context={'errors': lform.errors})


def user_logout(request):
    request.session.flush()
    return redirect(reverse('index'))


def user_retrieve(request):
    if request.method == 'GET':
        return render(request, 'user/forgot-password.html')
    else:
        return HttpResponse(request.POST.get('email-or-tel'))


def user_center(request):
    return HttpResponse("用户中心")


def reset_password(request):
    return render(request, 'user/reset-password.html')


def post_blog(request):
    if request.method == 'GET':
        return redirect(reverse('index'))
    else:
        pass #TODO post微博
