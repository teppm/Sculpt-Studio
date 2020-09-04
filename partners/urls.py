from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.partners, name='partners'),
    path('add_partners/', views.add_partners, name='add_partners'),
    path('edit_partners/<int:partner_id>', views.edit_partners, name='edit_partners'),
]