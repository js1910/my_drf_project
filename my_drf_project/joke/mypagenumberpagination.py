# 分页
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

# 普通分页
# class MyPageNumberPagination(PageNumberPagination):
#     page_size = 2
#     max_page_size = 5
#     page_size_query_param = 'size'
#     page_query_param = 'page'
#
#     '''
#     age_query_param：表示url中的页码参数
# 		page_size_query_param：表示url中每页数量参数
# 		page_size：表示每页的默认显示数量
# 		max_page_size：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
#     '''


# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 2
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 5
# #
# #     '''
# #     default_limit：表示默认每页显示几条数据
# # 		limit_query_param：表示url中本页需要显示数量参数
# # 		offset_query_param：表示从数据库中的第几条数据开始显示参数
# # 		max_limit：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
# #     '''
#
# class MyPageNumberPagination(CursorPagination):
#     cursor_query_param = 'cursor'
#     page_size = 1
#     ordering = 'id'
#     page_size_query_param = 'size'
#     max_page_size = 1
#
#     '''
#     cursor_query_param：表示url中页码的参数
# 		page_size_query_param：表示每页显示数据量的参数
# 		max_page_size：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
# 		ordering：表示返回数据的排序方式
#     '''
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from .custom_json_response import JsonResponse
from rest_framework import status



class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 10
    page_size_query_param = 'size'
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
                            previous=self.get_previous_link(), count=self.page.paginator.count)

#
# class MyPageNumberPagination(LimitOffsetPagination):
#     default_limit = 1
#     limit_query_param = 'limit'
#     offset_query_param = 'offset'
#     max_limit = 2
#
#     def get_paginated_response(self, data):
#         return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
#                             previous=self.get_previous_link(), count=self.count)
#
#
# class MyPageNumberPagination(CursorPagination):
#     cursor_query_param = 'cursor'
#     page_size = 1
#     ordering = 'id'
#     page_size_query_param = 'size'
#     max_page_size = 1
#
#     def get_paginated_response(self, data):
#         return JsonResponse(data=data, code=200, msg="success", status=status.HTTP_200_OK, next=self.get_next_link(),
#                             previous=self.get_previous_link())
