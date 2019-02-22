from django.db import models


class BaseModel(models.Model):
    insertTime = models.DateTimeField(auto_now_add=True, verbose_name='插入时间')
    opertionTime = models.DateTimeField(auto_now_add=True, verbose_name='更新时间')
    isdelete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        abstract = True
