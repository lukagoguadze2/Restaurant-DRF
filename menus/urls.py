from django.urls import path
from .views import SubCategoryListView, DishListView

app_name = 'menus'

urlpatterns = [
    path('sub-categories/', SubCategoryListView.as_view(), name='sub-category-list'),
    path('dishes/', DishListView.as_view(), name='dish-list'),
]
