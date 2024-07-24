from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_course_update_info(email_list, name):
    """Отправляет сообщение пользователям об обновлении курса"""
    send_mail(
        "Курс обновлен.",
        f"Курс: {name} обновлен.",
        settings.EMAIL_HOST_USER,
        email_list,
    )
