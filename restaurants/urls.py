from django.urls import path
from .views import RestaurantListView, MainCategoryListView

app_name = 'restaurants'

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant-list'),
    path('main-categories/', MainCategoryListView.as_view(), name='main-category-list'),
]
