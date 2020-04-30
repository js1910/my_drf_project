

from django.urls import path,include
from app04 import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('games/', views.GameList.as_view(),name='game-list'),
    path('games/<int:pk>/', views.GameDetail.as_view(),name='game-detail'),

    path('news/', views.NewList.as_view(), name='new-list'),
    path('news/<int:pk>/', views.NewDetail.as_view(), name='new-detail'),

    path('login/', views.Login.as_view(), name='login'),

    path('carts/', views.CartList.as_view(), name='carts'),

    path('api-token-auth/', obtain_jwt_token),
]
