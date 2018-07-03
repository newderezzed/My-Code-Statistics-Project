import redis
from django.shortcuts import render,HttpResponse
from utils.redis_pool import POOL

def index(request):
    conn = redis.Redis(connection_pool=POOL)
    conn.hset('kkk','age',18)

    return HttpResponse('设置成功')
def order(request):
    conn = redis.Redis(connection_pool=POOL)
    conn.hget('kkk','age')

    return HttpResponse('获取成功')