from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:menu_name>/', views.menu_view, name='menu_view'),
]
