## 本周作业

**使用 Django 的 Form、Auth 组件，实现用户登录和密码验证功能。**

### **作业要求：**

1. 登录界面要求能够输入用户名、密码，且密码需大于 8 位。
2. 用户名、密码通过     Django 的 Auth 组件对数据库中预先存储的用户密码进行验证。
3. 如果登录失败提示用户密码错误，登录成功后跳转到首页（或其他非登录的页面）。

### **完成情况：**

![](https://github.com/fengxiao/Python001-class01/blob/master/week09/picfornote/homeworkresult.jpg)

### **实现思路**

#### 第1步：创建 index App

在原第六个作业基础上创建 index App

cd D:\GitReposity\Python001-class01\week09\MyDjango

python manage.py startapp index

#### 第2步：配置setting.py

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #### 注册自己的APP
    'index',
    'Douban',
]
```

#### **第3步：参考Django官方的登陆窗口功能，制作新的登陆页面mylogin.html**

```
<!DOCTYPE html>
<html lang="en-us">
<head>
    <title>登陆Django系统</title>
    <link rel="stylesheet" href="/static/css/base.css">
    <link rel="stylesheet" href="/static/css/login.css">
    <link rel="stylesheet" href="/static/css/responsive.css">
    <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <meta name="robots" content="NONE,NOARCHIVE">
</head>

<body class=" login"  data-admin-utc-offset="0">
<!-- Container -->
<div id="container">
    <!-- Header -->
    <div id="header">
        <div id="branding">
            <h1 id="site-name">欢迎来到Django世界</a></h1>
        </div>
    </div>
    <!-- END Header -->
    <!-- Content -->
    <div id="content" class="colM">
        {% if is_error %}
            <p class="errornote" align="center" >请输入有效的用户名和密码！</p>
        {% endif %}
        <div id="content-main">
            <form action="/mylogin" method="post" id="login-form">
                {% csrf_token %}
                <div class="form-row">
                    <label class="required" for="id_username">用户名:</label>
                    <input type="text" name="username" autofocus required id="id_username">
                </div>
                <div class="form-row">
                    <label class="required" for="id_password">密 码:</label>
                    <input type="password" name="password" minlength="8" required id="id_password">
                </div>
                <div class="submit-row">
                    <label>&nbsp;</label><input type="submit" value="登陆">
                </div>
            </form>
        </div>
        <br class="clear">
    </div>
    <!-- END Content -->
    <div id="footer"></div>
</div>
<!-- END Container -->
</body>
</html>

```

#### **第4步：在index app下创建form.py**

```
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
```



#### **第5步：在index view.py下创建mylogin方法**

```
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
```

#### **第6步：配置路由**

在\MyDjango\MyDjango\urls.py下include index模块

```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('douban/',include('Douban.urls')),
    path('',include('index.urls')),
]

```

在MyDjango\index\urls.py下配置index模块的路由

```
from django.urls import path, re_path, register_converter
from . import views

urlpatterns = [
    path('', views.index),
    path('mylogin', views.mylogin)
]

```

