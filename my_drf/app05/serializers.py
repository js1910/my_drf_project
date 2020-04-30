from rest_framework import serializers
from .models import Tags,Category,News
from rest_framework.views import APIView
import re

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class NewSerializer(serializers.ModelSerializer):

    # updated_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # created_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # isdelete = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = News
        fields = '__all__'
        # 设置属性只读
        extra_kwargs ={
            "user":{"read_only":True}
        }

    # def get_isdelete(self,obj):
    #     # if obj.isdelete:
    #     #     return 1
    #     # else:
    #     #     return 0
    #     return 1 if obj.isdelete else 0

    def to_representation(self, instance):
        representation = super(NewSerializer,self).to_representation(instance)
        representation['category'] = instance.category.desc#CategorySerializer(instance.category).data
        # representation['user'] = instance.category.desc
        representation['tag'] = TagsSerializer(instance.tag,many=True).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'























