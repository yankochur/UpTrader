from django.shortcuts import render
from .models import MenuItem


def menu_view(request, menu_name):
    try:
        selected_item = MenuItem.objects.get(url=menu_name)
    except MenuItem.DoesNotExist:
        selected_item = None

    root_menu_items = MenuItem.objects.filter(parent=None)

    return render(request, 'menu/menu.html', {'root_menu_items': root_menu_items, 'menu_name': menu_name, 'selected_item': selected_item})


def index(request):
    return render(request, 'menu/index.html')
