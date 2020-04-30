from rest_framework import serializers
from .models import *

# 普通的序列化
# class AtricleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True) # read_only=True 只读
#     title = serializers.CharField(max_length=100,required=True)
#     vum = serializers.IntegerField(required=True)
#     content = serializers.CharField(max_length=1000)
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.vum = validated_data.get('vum',instance.vum)
#         instance.content = validated_data.get('content',instance.content)
#         instance.save()
#         return instance

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id','title','vum','content')



