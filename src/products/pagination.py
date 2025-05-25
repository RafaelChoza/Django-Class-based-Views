from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class ProductPagination(PageNumberPagination):
    page_size = 5
    page_query_param = "p" #page
    max_page_size = 5
    last_page_strings = "end"

class ProductLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 7
    limit_query_param = "records"
    offset_query_param = "start"

class ProductCPagination(CursorPagination):
    page_size = 4
    cursor_query_param = "cur"
    ordering = "title"