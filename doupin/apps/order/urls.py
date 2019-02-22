from django.urls import path
from . import views

app_name = "order"
urlpatterns = [
    path('', views.OrderPlaceView.as_view(), name='place'),  # 提交订单页面显示
]