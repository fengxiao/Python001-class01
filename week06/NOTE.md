学习笔记

## 本周作业

**作业背景**

数据经过分析和清洗之后，需要使用适当的方式对数据进行展示，Web 就是当前最流行的展示方式之一。

**作业要求：**使用 Django 展示豆瓣电影中某个电影的短评和星级等相关信息：

1. 要求使用 MySQL 存储短评内容（至少 20 条）以及短评所对应的星级；
2. 展示高于 3 星级（不包括 3 星级）的短评内容和它对应的星级；
3. （选做)）在 Web 界面增加搜索框，根据搜索的关键字展示相关的短评。

### 第一部分：项目创建

#### 第1步：进入作业目录

cd D:\GitReposity\Python001-class01\week06

#### 第2步：创建 Django 项目

cd D:\GitReposity\Python001-class01\week06

django-admin startproject MyDjango

#### 第3步：创建 Douban App

cd D:\GitReposity\Python001-class01\week06\MyDjango

python manage.py startapp Douban

### 第二部分：基础配置

#### 第4步：配置setting.py

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)

 

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image004.jpg)

#### 第5步：定义models

 

```
from django.db import models

# Create your models here.
class T2(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField()
    short = models.CharField(max_length=1000)

    # 元数据，不属于任何一个字段的数据
    class Meta:
        managed = True
        db_table = 't2'
```

#### 第6步：配置__init__.py

```
import pymysql
pymysql.version_info=(1,3,13,"final",0)
pymysql.install_as_MySQLdb()
```

 

#### 第7步：由models生成mysql表

**1)**   **执行python manage.py makemigrations**

cd D:\GitReposity\Python001-class01\week06\MyDjango

python manage.py makemigrations

 

**2)**   **执行python manage.py migrate**

cd D:\GitReposity\Python001-class01\week06\MyDjango

python manage.py migrate

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image005.png)

#### 第8步：初始化t2表数据

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image007.jpg)

### 第三部分：路由+View+Template

#### 第9步：配置路由

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image009.jpg)

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image011.jpg)

#### 第10步：配置View

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image013.jpg)

#### 第11步：添加bootstrap资源

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image015.jpg)

#### 第12步：编辑模板

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image017.jpg)

#### 第13步：运行项目

cd D:\GitReposity\Python001-class01\week06\MyDjango

python manage.py runserver

![img](file:///C:/Users/ewha/AppData/Local/Temp/msohtmlclip1/01/clip_image019.jpg)