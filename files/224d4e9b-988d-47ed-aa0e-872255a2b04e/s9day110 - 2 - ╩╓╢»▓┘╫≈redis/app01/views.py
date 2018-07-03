import redis
from django.shortcuts import render,HttpResponse
from django_redis import get_redis_connection


def index(request):
    conn = get_redis_connection("default")
    return HttpResponse('设置成功')
def order(request):
    conn = get_redis_connection("back")
    return HttpResponse('获取成功')