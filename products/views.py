from rest_framework.generics import ListAPIView
from django.db.models import Q

from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductCursorPagination


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.GET.get("category")
        search = self.request.GET.get("search")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if category:
            queryset = queryset.filter(category=category)

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
            )

        if min_price:
            queryset = queryset.filter(
                price__gte=min_price
            )

        if max_price:
            queryset = queryset.filter(
                price__lte=max_price
            )

        return queryset.order_by(
            "-created_at",
            "-id"
        )