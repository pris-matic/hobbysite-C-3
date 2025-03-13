from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.items_list, name='items_list'),
    path('item/<int:id>/', views.item_details, name='item_details'),
]