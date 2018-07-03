from django.shortcuts import render,HttpResponse
import time


def index(request):
    ctime = str(time.time())
    return HttpResponse(ctime)

def order(request):
    ctime = str(time.time())
    return HttpResponse(ctime)