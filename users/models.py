from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = PhoneNumberField(
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        verbose_name="Город", blank=True, null=True, help_text="Введите город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
    )
    lesson = models.ForeignKey(
        Lesson,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
    )

    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата оплаты")
    payment_type = models.CharField(
        max_length=50,
        verbose_name="Способ оплаты",
        choices=(("Наличные", "Наличные"), ("Перевод на счет", "Перевод на счет")),
    )
    payment_amount = models.IntegerField(verbose_name="Сумма оплаты")

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
