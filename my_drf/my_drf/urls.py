"""my_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'groups',views.GroupViewSet)
router.register(r'students',views.StudentViewSet)
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include(router.urls)),
    path('app01/',include(('app01.urls','app01'),namespace='app01')),
    path('app02/',include(('app02.urls','app02'),namespace='app02')),
    path('app03/',include(('app03.urls','app03'),namespace='app03')),
    path('app04/',include(('app04.urls','app04'),namespace='app04')),
    path('app05/',include(('app05.urls','app05'),namespace='app05')),

    path('app05/<str:version>/', include(('app05.urls', 'app05'), namespace='app05')),
    path('api-auth/', include(('rest_framework.urls','app04'), namespace='rest_framework')),

path('docs/', include_docs_urls(title='测试平台接口文档'))

]
