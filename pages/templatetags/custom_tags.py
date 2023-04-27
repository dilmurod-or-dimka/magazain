from django import template
from pages.models import Category, Brand

register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag()
def get_brands():
    brands = Brand.objects.all()
    return brands
