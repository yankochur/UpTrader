from django import template
from ..models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.all()
    return {'menu_items': menu_items}
