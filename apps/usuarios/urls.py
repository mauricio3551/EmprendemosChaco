from django.urls import path
from .views import profile_list, home_view, search_results, item_list,detalle_item_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('profiles/', profile_list, name='profile_list'),
    path('items/', item_list, name='item_list'),  # Agregado para acceder a item_list
    path('search_results/', search_results, name='search_results'),
    path('item/<int:item_id>/', detalle_item_view, name='detalle_item'),
]
