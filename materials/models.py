from config.settings import AUTH_USER_MODEL
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name="Курс")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="materials/course/image",
        blank=True,
        null=True,
        verbose_name="Картинка",
    )

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name="Урок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="materials/lesson/image",
        blank=True,
        null=True,
        verbose_name="Картинка",
    )
    url = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
