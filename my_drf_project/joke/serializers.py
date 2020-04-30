from rest_framework import serializers
from .models import Cross,HotCross,PicturesCross,Goods

class CrossSerializer(serializers.ModelSerializer):

    # updated_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # created_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # isdelete = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cross
        fields = '__all__'

    def get_isdelete(self,obj):
        # if obj.isdelete:
        #     return 1
        # else:
        #     return 0
        return 1 if obj.isdelete else 0

class PicturesCrossSerializer(serializers.ModelSerializer):

    # updated_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # created_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # isdelete = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = PicturesCross
        fields = '__all__'


    def get_isdelete(self,obj):
        if obj.isdelete:
            return 1
        else:
            return 0


class HotCrossSerializer(serializers.ModelSerializer):

    # updated_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    # created_time = serializers.DateTimeField(format='%Y-%s-$d',read_only=True)
    isdelete = serializers.SerializerMethodField(read_only=True)
    istop = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = HotCross
        fields = '__all__'

    def get_isdelete(self,obj):
        # if obj.isdelete:
        #     return 1
        # else:
        #     return 0
        return 1 if obj.isdelete else 0
    def get_istop(self,obj):
        return 1 if obj.istop else 0


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'

        # extra_kwargs = {
        #     "user": {"read_only": True}
        # }
    # def to_representation(self, instance):
    #     representation = super(GoodsSerializer,self).to_representation(instance)
    #     # representation['cross'] = CrossSerializer(instance.cross).data
    #     representation['user'] = instance.user.username
    #     representation['cross'] = CrossSerializer(instance.cross,many=True).data
    #     representation['picturescross'] = PicturesCrossSerializer(instance.picturescross,many=True).data
    #     representation['hotcross'] = HotCrossSerializer(instance.hotcross,many=True).data
    #     return representation

















