from celery import shared_task

from users.models import User
from users.services import check_by_last_login_date


@shared_task
def block_user():
    """Блокирует пользователя"""
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login and check_by_last_login_date(user.last_login):
            user.is_active = False
            user.save()
