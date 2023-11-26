from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Paginator for recipes."""
    page_size_query_param = 'limit'
