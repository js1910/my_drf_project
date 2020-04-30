from django.shortcuts import render
from .models import *
from .serializers import CrossSerializer,HotCrossSerializer,PicturesCrossSerializer,GoodsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
from rest_framework import status
# Create your views here.



from .custom_model_view_set import CustomModelViewSet

class CrossSet(CustomModelViewSet):

        queryset = Cross.objects.all()
        serializer_class = CrossSerializer


class HotCrossSet(CustomModelViewSet):

        queryset = HotCross.objects.all()
        serializer_class = HotCrossSerializer


class PicturesCrossSet(CustomModelViewSet):

        queryset = PicturesCross.objects.all()
        serializer_class = PicturesCrossSerializer

class GoodsSet(CustomModelViewSet):
        permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
        authentication_classes = [JSONWebTokenAuthentication]

        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer

        # def create(self, request, *args, **kwargs):
        #         serializer = self.get_serializer(data=request.data)
        #
        #         for joke in serializer:
        #                 if joke.id in serializer:
        #                         return '你已经点过赞了'
        #                 else:
        #                         serializer.is_valid(raise_exception=True)
        #                         self.perform_create(serializer)
        #                         headers = self.get_success_headers(serializer.data)
        #                         return JsonResponse(data=serializer.data, msg="success", code=201, status=status.HTTP_201_CREATED,
        #                             headers=headers)



