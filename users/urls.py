from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import (
    UserCreateAPIView,
    UserUpdateAPIView,
    PaymentList,
    UserListAPIView,
    UserRetrieveAPIView,
    UserDestroyAPIView,
)
from users.apps import UsersConfig

app_name = UsersConfig.name
urlpatterns = [
    path("", UserListAPIView.as_view(), name="user_list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
    path("<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("<int:pk>/delete/", UserDestroyAPIView.as_view(), name="user_destroy"),
    # Платежи
    path("payments/", PaymentList.as_view(), name="payment_list"),
    # Авторизация и получение токенов
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
