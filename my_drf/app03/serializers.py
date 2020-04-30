from rest_framework import serializers
from .models import *
import re

class UserSerializer(serializers.ModelSerializer):
    pwd1 = serializers.CharField(max_length=16,write_only=True) # write_only=True 写的时候需要
    pwd = serializers.CharField(max_length=16,write_only=True) # write_only=True 写的时候需要
    # gender = serializers.CharField(source='get_gender_display') # 反序列化，变成只读的属性，不能传输数据
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(UserSerializer,self).to_representation(instance)
        representation['gender'] = instance.get_gender_display()
        return representation

    def validate_phone(self, phone):
        if re.match('1[3456789]\d{9}',phone):
            user = User.objects.filter(phone=phone).first()
            if user:
                raise serializers.ValidationError('手机号已被注册')
            return phone
        else:
            raise serializers.ValidationError('手机号不合法')

    def validate(self, attrs):
        if 'pwd' in attrs and 'pwd1' in attrs:
            pwd = attrs['pwd']
            pwd1 = attrs['pwd1']
            if pwd!=pwd1:
                raise serializers.ValidationError('两次密码不一样')

            if 'pwd1' in attrs:
                    attrs.pop('pwd1')
        return attrs























