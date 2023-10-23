from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            data["images"]["images"]
        })


class ProductResultsSetPagination(CustomPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 1000