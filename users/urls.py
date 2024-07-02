from django.urls import path
from users.views import UserCreateAPIView, UserUpdateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name
urlpatterns = [
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
]
