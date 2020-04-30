

from django.urls import path,include
from app05 import views
from rest_framework_jwt.views import obtain_jwt_token
game_list = views.NewsSet.as_view({
    'get': 'list',
    'post': 'create'
})
game_detail = views.NewsSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

from rest_framework.routers import DefaultRouter


route = DefaultRouter()
route.register('news',views.NewsSet)
urlpatterns = [
    path('tags/', views.TagsList.as_view(),name='tags-list'),
    path('tags/<int:pk>/', views.TagsDetail.as_view(),name='tags-detail'),

    # path('news/', views.NewList.as_view(), name='new-list'),
    # path('news/<int:pk>/', views.NewDetail.as_view(), name='new-detail'),

    # path('news/', game_list, name='category-list'),
    # path('news/<int:pk>/', game_detail, name='category-detail'),

    path('',include(route.urls)),

    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),

    path('parse/', views.ParserView.as_view(), name='parse'),

    path('api-token-auth/', obtain_jwt_token), # jwt验证
]
