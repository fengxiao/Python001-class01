from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.

from .form import LoginForm
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Hello 朋友！您已经成功登陆Django系统！欢迎来到 Django 首页!")

def mylogin(request):
    is_error = False
    # POST
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)
                # 重定向至首页
                return redirect('/')
            else:
                # return HttpResponse('登录失败')
                is_error = True
                return render(request, 'mylogin.html', {'is_error': is_error})
    # GET
    if request.method == "GET":
        return render(request, 'mylogin.html',{'is_error': is_error})
