from django.shortcuts import render
from django.http import JsonResponse
from .models import Users
from common import rsaen
from django.core.cache import cache
from django.views import View
import random


# Create your views here.
# 注册
class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.GET('username')
        pwd = request.POST.GET('password')
        password = rsaen.decrypt_data(pwd)
        email = request.POST.GET('email')
        phoneNo = request.POST.GET('phoneNo')
        yzm = request.POST.GET('yzm')
        rdyzm = cache.get(phoneNo)
        if yzm != rdyzm:
            return JsonResponse({'retMsg': '验证不正确'})
        user = Users.objects.filter(username=username)
        if len(user) > 0:
            return JsonResponse({'retCode': 0, 'retMsg': '用户名几存在'})
        Users.objects.create_user(username=username, password=password, email=email, phoneNo=phoneNo)
        return JsonResponse({'retCode': 1, 'retMsg': 'ssss'})


# 短信验证
class Yzm(View):
    def post(self, request):
        phoneNo = request.POST.get('phoneNo')
        exist = cache.get(phoneNo)
        if exist == None:
            cache.set(phoneNo, random.randint(100000, 1000000), 300)
            return JsonResponse({'retCode': 1})
        else:
            return JsonResponse({'retCode': 0})
