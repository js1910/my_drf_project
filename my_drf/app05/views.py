from django.shortcuts import render


from rest_framework import generics
from .models import *
from .serializers import TagsSerializer,NewSerializer,CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import IsOwnerOrReadOnly
from .throttle import VisitThrottle
# class NewList(generics.ListCreateAPIView):
#
#     throttle_classes = [VisitThrottle]
#     permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
#     authentication_classes = [JSONWebTokenAuthentication]
#     queryset = News.objects.all()
#     serializer_class = NewSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#
from .throttle import UserThrottle
# class NewDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     throttle_classes = [UserThrottle]
#     permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
#     authentication_classes = [JSONWebTokenAuthentication]
#
#     queryset = News.objects.all()
#     serializer_class = NewSerializer



class CategoryList(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagsList(generics.ListCreateAPIView):

    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    def get_queryset(self): # 重写get_queryset返回不同版本的数据
        if self.request.version == 'v1':
            return Tags.objects.all()
        elif self.request.version == 'v2':
            return Tags.objects.exclude(id=1).all()


class TagsDetail(generics.RetrieveUpdateDestroyAPIView):


    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


from rest_framework.parsers import FormParser, JSONParser, FileUploadParser, MultiPartParser
from django.http import HttpResponse
from rest_framework.views import APIView
# 当请求类型application/json request.post 是没有值的,用的解析器是JSONParser
# 当请求类型application/x-www-form-urlencoded request.post 有值,用的解析器是FormParser
# 当请求类型multipart/form-data request.post 有值,用的解析器是MultiPartParser


class ParserView(APIView):
    def post(self, request, *args, **kwargs):
        # print("body:", request.body.decode())
        print("content_type:", request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print("data:", request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print("POST:", request.POST)
        print("FILES:", request.FILES)

        return HttpResponse('响应')
from .custom_filter import NewFilter
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .custom_model_view_set import CustomModelViewSet
class NewsSet(CustomModelViewSet):
        throttle_classes = [UserThrottle]
        permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
        authentication_classes = [JSONWebTokenAuthentication]
        queryset = News.objects.all()
        serializer_class = NewSerializer


        filter_backends = (filters.SearchFilter,filters.OrderingFilter)
        # filter_fields = ('title','content') # 支持搜索字段
        # filterset_class = NewFilter

        # 搜索
        search_fields = ('title','content')

        # 排序
        ordering_fields = ['id']


        def perform_create(self, serializer):
            serializer.save(user=self.request.user)

        # def get_queryset(self):
        #     kw = self.request.query_params.get('kw')
        #
        #     if kw:
        #         return News.objects.filter(title__contains=kw).all()
        #     else:
        #         return News.objects.all()