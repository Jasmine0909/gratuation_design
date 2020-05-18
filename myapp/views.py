from django.shortcuts import render, redirect, HttpResponse
from myapp.models import User, Goods, Order
import hashlib

# Create your views here.


def homepage(request):
    if request.method == "GET":
        return render(request, "homepage.html")
        # return redirect(request, "/medicine")
    elif request.method == 'POST':
        # 首页中如果有Post的实现就是搜索功能
        try:
            content_info = request.POST
            content = content_info.get("content")
            if content == '':
                content = "人参"
            # 查找Goods表中的所有数据
            goods = Goods.objects.all()
            medicine = []
            for i in goods:
                if content in i.name or content in i.function.split('，'):
                    medicine.append(i)
        except:
            medicine = ''
        # research(request, medicine)
        return render(request, "research.html", context={"medicine": medicine})


def research(request, content):
    if request.method == "GET":
        try:
            if content == '':
                content = "人参"
            # 查找Goods表中的所有数据
            goods = Goods.objects.all()
            medicine = []
            for i in goods:
                if content in i.name or content in i.function.split('，'):
                    medicine.append(i)
        except:
            medicine = ''
        # print("***************", medicine)
        return render(request, "research.html", context={"medicine": medicine})


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
    elif request.method == "POST":
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


def shopping(request, user):
    if user == '':
        return HttpResponse('请先登录')
    else:
        order = Order.objects.all()
        goods = []
        medicine = []
        for i in order:
            if i.name == user:
                goods.append(i)
        for j in goods:
            message = Goods.objects.get(price=j.total)
            medicine.append(message)
        return render(request, "shopping.html", context={"medicine": medicine})


def details(request, num):
    if request.method == "GET":
        medicine = Goods.objects.get(id=num)
        return render(request, "details.html", context={"medicine": medicine})


def news(request):
    return render(request, "news.html")


def recommend(request):
    return render(request, "recommend.html")
