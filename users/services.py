from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from config import settings

import stripe

stripe.api_key = settings.STRIPE_API_KEY


def check_owner(self, request):
    """Проверяет владельца"""
    user = self.get_object()
    if request.user == user:
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    else:
        raise PermissionDenied


def create_stripe_product(product):
    """Создает продукт в страйпе"""
    return stripe.Product.create(name=product)


def create_stripe_price(amount, product):
    """Создает цену в страйпе"""
    product_name = "Не указано"
    if product:
        product_name = product.name
    return stripe.Price.create(
        currency="usd", unit_amount=amount * 100, product_data={"name": product_name}
    )


def create_stripe_session(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
