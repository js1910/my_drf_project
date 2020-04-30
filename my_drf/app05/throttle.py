from rest_framework.throttling import SimpleRateThrottle

class VisitThrottle(SimpleRateThrottle):
    scope = '未认证用户'
    def get_cache_key(self, request, view):
        return self.get_ident(request)

class UserThrottle(SimpleRateThrottle):
    scope = '已认证用户'
    def get_cache_key(self, request, view):
        return request.user