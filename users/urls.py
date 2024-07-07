from django.urls import path
from users.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    PaymentList,
    UserListAPIView,
)
from users.apps import UsersConfig

app_name = UsersConfig.name
urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),

    # Платежи
    path("payments/", PaymentList.as_view(), name="payment_list"),
]
