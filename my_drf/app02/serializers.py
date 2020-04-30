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

# class ArticleSerializer(serializers.ModelSerializer):
#
#     # StringRelatedField
#     # category = serializers.StringRelatedField()
#     # 如果序列化转成字符串，那么数剧变成只读的形式，不能传输，不支持反序列化
#
#     # PrimaryKeyRelatedField
#     # category = serializers.PrimaryKeyRelatedField(read_only=True)
#     # 如果多个需要加many=True read_only=True
#     # 如果单个需要加 read_only=True
#
#     # HyperlinkedRelatedField 显示超链接
#     # category = serializers.HyperlinkedRelatedField(
#     #     read_only=True,
#     #     view_name='app02:category-detail',  # 路由的别名
#     #     lookup_field='pk',  # 数据库字段的名字
#     #     lookup_url_kwarg="pk"  # 路由中参数的名字
#     # )
#
#     # SlugRelatedField 显示任意一个属性
#     # category = serializers.SlugRelatedField(
#     #     read_only=True,
#     #     slug_field='name'
#     # )
#
#     # HyperlinkedIdentityField 返回指定的超链接字段
#     # category = serializers.HyperlinkedIdentityField(
#     #     read_only=True,
#     #     view_name='app02:category-detail',
#     #     lookup_field='pk',
#     #     lookup_url_kwarg='pk'
#     #
#     # )
#
#
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#         # fields = ('id','title','content','cate')
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     # articles = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
#
#     # HyperlinkedRelatedField 显示超链接
#     # articles = serializers.HyperlinkedRelatedField(
#     #     many=True,
#     #     read_only=True,
#     #     view_name='app02:article-detail',  # 路由的别名
#     #     lookup_field='pk',  # 数据库字段的名字
#     #     lookup_url_kwarg="pk"  # 路由中参数的名字
#     # )
#
#     # SlugRelatedField 显示任意的一个属性
#     # articles = serializers.SlugRelatedField(
#     #     read_only=True,
#     #     slug_field='title',
#     #     many=True
#     # )
#
#     # HyperlinkedIdentityField 显示指定的超链接
#     # articles = serializers.HyperlinkedIdentityField(
#     #     read_only=True,
#     #     view_name='app02:category-detail',
#     #     lookup_field='pk',
#     #     lookup_url_kwarg='pk',
#     #     many=True
#     # )
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#         # fields = ('id','name','articles')

# -------------------------------------------------------------------------------------------------------------->>>>>>>>
# HyperlinkedModelSerializer
# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#         extra_kwargs = {
#             'url': {'view_name': 'app02:article-detail', 'lookup_field': 'pk','lookup_url_kwarg':'pk'},
#             'category': {'view_name': 'app02:category-detail', 'lookup_field': 'pk','lookup_url_kwarg':'pk'},
#         }
#
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'articles')
#
#         extra_kwargs = {
#             'url': {'view_name': 'app02:category-detail', 'lookup_field': 'pk','lookup_url_kwarg':'pk'},
#             'articles': {'view_name': 'app02:article-detail', 'lookup_field': 'pk','lookup_url_kwarg':'pk'},
#         }

# ---------------------------------------------------------------------------------------------------------------->>>>>>

# 序列化嵌套

# class CategorySerializer(serializers.ModelSerializer):
#     # articles = ArticleSerializer(many=True)
#     class Meta:
#         model = Category
#         fields = '__all__'
#
# class ArticleSerializer(serializers.ModelSerializer):
#     category = CategorySerializer()
#
#     class Meta:
#         model = Article
#         fields = '__all__'

# -------------------------------------------------------------------------------------------------------------->>>>>>>>

# 深度
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         depth = 1

# ------------------------------------------------------------------------------------------------------------->>>>>>>>>
# SerializerMethodField 自定义

# class CategorySerializer(serializers.ModelSerializer):
#     count = serializers.SerializerMethodField()
#     class Meta:
#         model = Category
#         fields = '__all__'
#     def get_count(self,obj): # obj 当前分类的对象
#         return obj.articles.count()
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'

# ------------------------------------------------------------------------------------------------------------->>>>>>>>>
# source 序列化的时候指定数据源
# class MyListField(serializers.CharField):
#     def to_representation(self, value):
#         data_list = []
#         for row in value:
#             data_list.append({'title':row.title,'content':row.content})
#             return data_list
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = MyListField(source='articles.all')
#     class Meta:
#         model = Category
#         fields = '__all__'
#
# class ArticleSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(source='category.name')
#     class Meta:
#         model = Article
#         fields = '__all__'

# ---------------------------------------------------------------------------------------------------------------->>>>>>
# to_representation 序列化器的每个字段实际都是由该字段类型的to_representation方法决定格式的，可以通过重写该方法来决定格式。

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
    def to_representation(self, instance):# 只影响序列化，支持反序列化
        representation = super(CategorySerializer,self).to_representation(instance) # 先调用父类  instance： 当前数据
        representation['articles'] = ArticleSerializer(instance.articles,many=True).data
        # representation['articles'] = instance.article.name
        # representation['articles'] = instance.category.id
        return representation


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        # depth = 1

    # def to_representation(self, instance):# 只影响序列化，支持反序列化
    #     representation = super(ArticleSerializer,self).to_representation(instance) # 先调用父类  instance： 当前数据
    #     # representation['category'] = CategorySerializer(instance.category).data
    #     representation['category'] = instance.category.name
    #     # representation['category'] = instance.category.id
    #     return representation
























