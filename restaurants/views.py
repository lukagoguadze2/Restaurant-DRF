from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Restaurant, MainCategory
from .serializers import RestaurantSerializer, MainCategorySerializer


class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_context(self):
        return {'request': self.request}


class MainCategoryListView(generics.ListCreateAPIView):
    queryset = MainCategory.objects.all()
    serializer_class = MainCategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        return {'request': self.request}
