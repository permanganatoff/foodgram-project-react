from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Foo."""
    page_size_query_param = 'limit'
