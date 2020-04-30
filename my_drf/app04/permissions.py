from rest_framework.permissions import BasePermission

# 自定义判断用户是否有权限修改

class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        else:
            return False

