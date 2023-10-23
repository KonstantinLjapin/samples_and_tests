from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },


            'currentPage': self.page.number,
            'lastPage': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'items': data
        })


class CatalogResultsSetPagination(CustomPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 1000