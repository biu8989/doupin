from django.db import models
from common.BaseModel import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser, BaseModel):
    phoneNo = models.CharField(max_length=50, verbose_name='手机号')

    class Meta:
        db_table = 'demo_user'
        verbose_name = '用户表'


class Address(BaseModel):
    user = models.ForeignKey(Users, verbose_name='所属账户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    province = models.CharField(max_length=20, verbose_name='省')
    city = models.CharField(max_length=20, verbose_name='市')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = "demo_address"
        verbose_name = "地址表"
