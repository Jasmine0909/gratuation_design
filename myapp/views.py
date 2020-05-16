from django.shortcuts import render, redirect
from myapp.models import User, Goods
import hashlib

# Create your views here.


def homepage(request):
    if request.method == "GET":
        return render(request, "homepage.html")
        # return redirect(request, "/medicine")
    elif request.method == 'POST':
        research(request)


def research(request):
    word = request.POST

    pass


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_info = request.POST
        username = user_info.get("username")
        password = user_info.get("password")
        try:
            name = User.objects.get(username=username)
            password_database = name.password

            obj = hashlib.md5()
            obj.update(password.encode('utf8'))
            password_md5 = obj.hexdigest()

            if password_database == password_md5:
                # 登录成功，记录下用户名,返回首页
                return render(request, "homepage.html")
            else:
                # 返回密码错误，重新输入
                return render(request, 'login.html', context={"username": username, "is_login": "password_error"})
        except:
            # 返回用户名不存在
            return render(request, 'login.html', context={"username": username, "is_login": "username_not_exist"})


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        user_info = request.POST
        # telephone = user_info.get("telephone")
        username = user_info.get("username")
        password = user_info.get("password")
        password_again = user_info.get("password_again")
        if username == '':
            # 用户名为空
            return render(request, 'register.html', context={'is_register': 'username_none'})
        elif password == '' or password_again == '':
            # 密码为空
            return render(request, 'register.html', context={'is_register': 'password_none'})
        else:
            try:
                # 用户名已存在在数据库中
                User.objects.get(username=username)
                return render(request, 'register.html', context={"username": username, "is_register": 'username_exist'})
#
            except:
                # 两次输入的密码不一致
                if password != password_again:
                    return render(request, 'register.html',
                                  context={"username": username, "is_register": 'password_different'})
                else:
                    obj = hashlib.md5()
                    obj.update(password.encode('utf8'))
                    password_md5 = obj.hexdigest()
                    # 将加密后的密码和对应账号存入数据库中
                    User.objects.create(username=username, password=password_md5)
                    return render(request, 'homepage.html', context={'username': username})


def shopping(request):
    return render(request, "shopping.html")


def details(request):
    if request.method == "GET":
        return render(request, "details.html")
    elif request.method == "POST":
        # 实现将此商品的信息存入数据库的功能，前端界面保持不动，只出现弹窗
        # return render(request, "details.html")
        pass


def news(request):
    return render(request, "news.html")


def recommend(request):
    return render(request, "recommend.html")
