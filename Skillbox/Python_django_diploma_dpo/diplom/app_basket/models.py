from decimal import Decimal
from django.db import models
from django.conf import settings
from app_products.models import Product


class Cart:
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def clear(self):
        # Обновление сессии cart
        self.clear()
        self.delete()
        self._session_key = None

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def add(self, product, count=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"id": product_id,
                                     "category": product.category.pk,
                                     "price": str(product.price),
                                     "count": 1,
                                     "date": str(product.date),
                                     "title": product.title,
                                     "description": product.description,
                                     "fullDescription": product.fullDescription,
                                     "href": product.href,
                                     "freeDelivery": product.freeDelivery,
                                     "reviews": len(product.reviews.all()),
                                     "rating": float(product.rating)
                                     }

        total = product.price * self.cart[product_id].get('count')
        self.cart[product_id]['price'] = str(total)
        self.save()

