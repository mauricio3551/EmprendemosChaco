from django.urls import path
from .views import profile_list, home_view, search_results, item_list,detalle_item_view,categoria_view,pintura_1_view,pintura_2_view,item_form_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home_view'),
    path('profiles/', profile_list, name='profile_list'),
    path('items/', item_list, name='item_list'),  # Agregado para acceder a item_list
    path('search_results/', search_results, name='search_results'),
    path('item/<int:item_id>/', detalle_item_view, name='detalle_item'),
    path('categoria/<str:categoria>/', categoria_view, name='categoria_view'),
    path('pintura_1/', pintura_1_view, name='pintura_1'),
    path('pintura_2/', pintura_2_view, name='pintura_2'),
    
    # Nuevas URLs para agregar y editar ítems
    path('item/new/', item_form_view, name='item_new'),  # URL para crear un nuevo ítem
    path('item/edit/<int:item_id>/', item_form_view, name='item_edit'),  # URL para editar un ítem existente
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)