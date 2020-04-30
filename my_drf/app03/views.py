
from .models import *
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.parsers import JSONParser
# Create your views here.
class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         ser = UserSerializer(instance=users,many=True, context={'request': request})
#         return JSONResponse(ser.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request) # 只能使用json方式传数据
#         ser = UserSerializer(data=data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data,status=201) # 状态码201 代表创建成功
#         else:
#             return JsonResponse(ser.errors,status=400)
#
# def user_detail(request,pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return HttpResponse('url not found',status=404)
#
#     if request.method == 'GET':
#         ser = UserSerializer(instance=user, context={'request': request})
#         return JsonResponse(ser.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request) # 要更新的数据
#         ser = UserSerializer(instance=user,data=data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data,status=201)
#         return JsonResponse(ser.errors,status=400)
#
#     elif request.method == 'PATCH':
#         data = JSONParser().parse(request)  # 要更新的数据
#         ser = UserSerializer(instance=user, data=data,partial=True, context={'request': request}) # partial=True 局部更新
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data, status=201)
#         return JsonResponse(ser.errors, status=400)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return HttpResponse(status=204) # 删除成功


# from rest_framework.decorators import api_view # 加了@api_view(['GET','POST']) request就变成了drf中的request
# from rest_framework.response import Response # 返回数据
# from rest_framework import status # 状态码
# @api_view(['GET','POST'])
# def user_list(request):
#     if request.method == 'GET':
#         users = User.objects.all()
#         ser = UserSerializer(instance=users, many=True, context={'request': request})
#         return Response(ser.data)
#
#     elif request.method == 'POST':
#         ser = UserSerializer(data=request.data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)  # 状态码201 代表创建成功
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
# from rest_framework.views import APIView
# from django.http import Http404
# class UserDetail(APIView):
#     def get_user(self,pk):
#         try:
#             user = User.objects.get(pk=pk)
#             return user
#         except User.DoesNotExist:
#             raise Http404()
#     def get(self,request,*args,**kwargs):
#         id = kwargs.get('pk')
#         user = self.get_user(id)
#         ser = UserSerializer(instance=user, context={'request': request})
#         return Response(ser.data)
#
#     def put(self,request,*args,**kwargs):
#         id = kwargs.get('pk')
#         user = self.get_user(id)
#         ser = UserSerializer(instance=user, data=request.data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,*args,**kwargs):
#         id = kwargs.get('pk')
#         user = self.get_user(id)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  # 删除成功
#
#     def patch(self,request,*args,**kwargs):
#         id = kwargs.get('pk')
#         user = self.get_user(id)
#         ser = UserSerializer(instance=user, data=request.data, partial=True, context={'request': request})  # partial=True 局部更新
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
#

# 类视图
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,mixins,generics
# class UserList(APIView):
#     def get(self,request,*args,**kwargs):
#         user = User.objects.all()
#         ser = UserSerializer(instance=user,many=True,context={'request':request})
#         return Response(ser.data)
#
#     def post(self,request,*args,**kwargs):
#         ser = UserSerializer(data=request.data, context={'request': request})
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = User.objects.all() # 数据源
#     serializer_class = UserSerializer # 序列化类
#     def get(self,request,*args,**kwargs):
#         return super().list(request,*args,**kwargs)
#
#     def post(self,request,*args,**kwargs):
#         return super().create(request,*args,**kwargs)
#
# class UserDetail(mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#
#     queryset = User.objects.all() # 数据源
#     serializer_class = UserSerializer # 序列化类
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)
#
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
