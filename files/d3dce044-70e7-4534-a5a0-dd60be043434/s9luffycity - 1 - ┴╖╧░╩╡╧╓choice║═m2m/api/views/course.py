from rest_framework.views import APIView
from rest_framework.response import Response
from api import models

from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"

# class CourseDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.CourseDetail
#         fields = "__all__"
#         depth = 1 # 0-10

class CourseDetailSerializer(serializers.ModelSerializer):

    # one2one/fk/choice
    title = serializers.CharField(source='course.title')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')

    # m2m
    recommends = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['course','title','img','level','slogon','why','recommends']


    def get_recommends(self,obj):
        # 获取推荐的所有课程
        queryset = obj.recommend_courses.all()

        return [{'id':row.id,'title':row.title} for row in queryset]

# 方式一：
# class CourseView(APIView):
#
#     def get(self,request,*args,**kwargs):
#
#         ret = {'code':1000,'data':None}
#
#         try:
#             pk = kwargs.get('pk')
#             if pk:
#                 obj = models.Course.objects.filter(id=pk).first()
#                 ser = CourseSerializer(instance=obj,many=False)
#             else:
#                 queryset = models.Course.objects.all()
#                 ser = CourseSerializer(instance=queryset,many=True)
#             ret['data'] = ser.data
#         except Exception as e:
#             ret['code'] = 1001
#             ret['error'] = '获取课程失败'
#
#         return Response(ret)



# 方式二
# View
# APIView
# GenericAPIView
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
class CourseView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}

        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}

        try:
            # 课程ID=2
            pk = kwargs.get('pk')

            # 课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=pk).first()

            ser = CourseDetailSerializer(instance=obj,many=False)

            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)


def test(request,*args,**kwargs):
    from django.shortcuts import HttpResponse
    obj = models.Course.objects.filter(id=2).first()
    print(obj.title)
    print(obj.level) #
    print(obj.get_level_display() ) #
    return HttpResponse('...')










