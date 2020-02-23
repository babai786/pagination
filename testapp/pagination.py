from rest_framework.pagination import  PageNumberPagination,LimitOffsetPagination,CursorPagination


class Mypagination1(PageNumberPagination):
    page_size =  3
    page_query_param = 'mypage'
    page_size_query_param = 'num'
    max_page_size = 15


class Mypagination2(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 9


class Mypagination3(CursorPagination):
    ordering = '-eno'
    page_size = 2