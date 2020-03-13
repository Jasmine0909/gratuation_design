from django.shortcuts import render, redirect

# Create your views here.


def homepage(request):
    if request.method == "GET":
        return render(request, "homepage.html")
        # return redirect(request, "/medicine")
    else:
        return render(request, "register.html")


def login(request):
    return render(request, 'login.html')
    pass


def register(request):
    # print("注册")
    # if request.method == "GET":
    return render(request, "register.html")
    # elif request.method == "POST":
    #     user_info = request.POST
    #     username = user_info.get("username")
    #     password = user_info.get("password")
    #     password_again = user_info.get("password_again")
#         if username == '':
#             # 用户名为空
#             return render(request, 'register.html', context={'is_login': 'n0'})
#         elif password == '' or password1 == '':
#             # 密码为空
#             return render(request, 'register.html', context={'is_login': 'n1'})
#         else:
#             try:
#                 # 用户名已存在
#                 Login.objects.get(username=username)
#                 return render(request, 'register.html', context={"username": username, "is_login": 0})
#
#             except:
#                 # 两次输入的密码不一致
#                 if password != password1:
#                     return render(request, 'register.html', context={"username": username, "is_login": 1})
#                 else:
#                     s = hashlib.sha1()
#                     s.update(password.encode("utf-8"))
#                     password = s.hexdigest()
#                     # print(password)
#                     Login.objects.create(username=username, password=password)
#                     # return render(request, 'myblog/login.html', context={'is_login': 2})
#                     return redirect("/expapp/login_redict")


def shopping(request):
    return render(request, "shopping.html")


def details(request):
    render(request, "details.html")
