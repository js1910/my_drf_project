from django.shortcuts import render
from .models import *
from .serializers import ArticleSerializer,CategorySerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse,Http404
from rest_framework.parsers import JSONParser

# Create your views here.
class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def article_list(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        ser = ArticleSerializer(instance=arts,many=True, context={'request': request})
        return JSONResponse(ser.data)
        #
        # content = JSONRenderer().render(ser.data)
        # json_data = str(content,encoding='utf-8')
        #
        # return JsonResponse(json_data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) # 只能使用json方式传数据
        ser = ArticleSerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201) # 状态码201 代表创建成功
        else:
            return JsonResponse(ser.errors,status=400)

def article_detail(request,pk):
    try:
        art = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse('url not found',status=404)

    if request.method == 'GET':
        ser = ArticleSerializer(instance=art, context={'request': request})
        return JsonResponse(ser.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request) # 要更新的数据
        ser = ArticleSerializer(instance=art,data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        return JsonResponse(ser.errors,status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)  # 要更新的数据
        ser = ArticleSerializer(instance=art, data=data,partial=True, context={'request': request}) # partial=True 局部更新
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

    elif request.method == 'DELETE':
        art.delete()
        return HttpResponse(status=204) # 删除成功


def category_list(request):
    if request.method == 'GET':
        arts = Category.objects.all()
        ser = CategorySerializer(instance=arts,many=True, context={'request': request})
        return JSONResponse(ser.data)
        #
        # content = JSONRenderer().render(ser.data)
        # json_data = str(content,encoding='utf-8')
        #
        # return JsonResponse(json_data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request) # 只能使用json方式传数据
        ser = CategorySerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201) # 状态码201 代表创建成功
        else:
            return JsonResponse(ser.errors,status=400)

def category_detail(request,pk):
    try:
        cat = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse('url not found',status=404)

    if request.method == 'GET':
        ser = CategorySerializer(instance=cat, context={'request': request})
        return JsonResponse(ser.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request) # 要更新的数据
        ser = CategorySerializer(instance=cat,data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data,status=201)
        return JsonResponse(ser.errors,status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)  # 要更新的数据
        ser = CategorySerializer(instance=cat, data=data,partial=True, context={'request': request}) # partial=True 局部更新
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

    elif request.method == 'DELETE':
        cat.delete()
        return HttpResponse(status=204) # 删除成功