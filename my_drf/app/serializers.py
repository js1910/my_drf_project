from rest_framework import serializers
from .models import *
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        # fields = ('id','name','age','group')
        fields = '__all__' # 也可以返回所有的信息
