from django.db import models
from utils.basemodel import BaseModel

class OrderInfo(BaseModel):
    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成')
    )
    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单id')
    # user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    # addr = models.ForeignKey(Address, verbose_name='地址', on_delete=models.CASCADE)
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单运费')
    order_status = models.IntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, default='', verbose_name='支付编号')

    class Meta:
        db_table = 'demo_order_info'
        verbose_name = '订单'



class OrderGoods(BaseModel):
    '''订单商品模型类'''
    order = models.ForeignKey(OrderInfo, verbose_name='订单', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name='商品数目')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    comment = models.CharField(max_length=256, default='', verbose_name='评论')


    class Meta:
        db_table = 'demo_order_goods'
        verbose_name = '订单商品'
