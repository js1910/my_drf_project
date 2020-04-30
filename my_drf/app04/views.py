
from rest_framework import generics
from .models import Game,News
from .serializers import GameSerializer,NewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    permission_classes = [IsAuthenticatedOrReadOnly,]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    # IsAuthenticatedOrReadOnly 判断用户是否登陆 IsOwnerOrReadOnly 判断用户是否有权限修改数据
    # ，即自己的数据
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]
    # permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]
    authentication_classes = [JSONWebTokenAuthentication]
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class NewList(generics.ListCreateAPIView):
    # 局部认证大于全局认证
    permission_classes = [IsAuthenticated] # 用户存在并且是激活的状态
    # authentication_classes = [SessionAuthentication] # 采用session加密认证
    authentication_classes = [BasicAuthentication] # 采用base64加密认证
    queryset = News.objects.all()
    serializer_class = NewSerializer


class NewDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]
    authentication_classes = [JSONWebTokenAuthentication]
    queryset = News.objects.all()
    serializer_class = NewSerializer

from rest_framework.views import APIView
from django.http import JsonResponse
from .models import User,UserToken

import time,hashlib

def get_md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(str(user),encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()

class Login(APIView):
    def post(self,request,*args,**kwargs):
        ret = {'code':1,'msg':'','data':{}}
        # request drf中的request _request django中的request
        username = request.POST.get('username')
        password = request._request.POST.get('password')
        user = User.objects.filter(username=username,password=password).first()
        if not user:
            ret['code'] = -1
            ret['msg'] = '用户不存在'
        else:
            token = get_md5(user)
            UserToken.objects.update_or_create(user=user,defaults={'token':token})
            ret['data']['token'] = token
        return JsonResponse(ret)


from rest_framework.permissions import BasePermission
from rest_framework import exceptions
# 自定义验证
class MyAuthtication(BasicAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN')
        usertoken = UserToken.objects.filter(token=token).first()
        if usertoken:
            return (usertoken.user,token)
        else:
            raise exceptions.AuthenticationFailed('认证失败')

class MyPermission(BasePermission):
    def has_permission(self,request,view):
        if not request.user:
            return False
        return True

class CartList(APIView):
#     permission_classes = [MyPermission]
#     authentication_classes = [MyAuthtication]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]
    def post(self,request,*args,**kwargs):
        ret = {'code':1,'msg':'','data':{
            'goods':[
                {'name':'苹果','price':12},
                {'name':'苹果','price':13},
                {'name':'苹果','price':14}
            ]
        }}
        return JsonResponse(ret)












