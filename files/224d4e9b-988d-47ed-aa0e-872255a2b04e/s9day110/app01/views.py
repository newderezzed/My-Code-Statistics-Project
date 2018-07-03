from django.shortcuts import render,HttpResponse
import time
from django.views.decorators.cache import cache_page
from rest_framework.throttling import SimpleRateThrottle

@cache_page(60 * 15)
def index(request):
    ctime = str(time.time())
    return HttpResponse(ctime)

def order(request):

    return render(request,'order.html')