from django_filters import rest_framework as filters
from .models import News


class NewFilter(filters.FilterSet):
    min_status = filters.NumberFilter(field_name='status', lookup_expr='gte')
    max_status = filters.NumberFilter(field_name='status', lookup_expr='lte')
    #根据名字过滤忽略大小写
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = filters.CharFilter(field_name='content', lookup_expr='icontains')
    # 自定义
    category = filters.NumberFilter(method='filter_category_id')
    def filter_category_id(self,queryset,name,value):
        return queryset.filter(category=value).all()
    # tags = filters.NumberFilter(method='filter_tags_id')
    # def filter_tags_id(self,queryset,name,value):
    #     return queryset.filter(tag=value).all()
    class Meta:
        model = News
        fields = ('min_status', 'max_status')  # 允许精准查询的字段
        search_fields = ('title','content','category','tag')  # 允许模糊查询的字段