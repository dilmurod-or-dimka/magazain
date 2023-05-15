from accounts.models import CustomUser
from pages.models import Product
from .models import Order, OrderProduct
from core import settings


class CartForAuthenticatedUser:
    pass


class CartForAnonymousUser:
    pass


def get_cart_data(request):
    pass
