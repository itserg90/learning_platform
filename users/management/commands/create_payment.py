from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.filter(pk=1).first()
        course = Course.objects.filter(pk=5).first()
        lesson = Lesson.objects.filter(pk=4).first()

        payment = Payment.objects.create(
            user=user, course=None, lesson=lesson, payment_type="Перевод на счет", payment_amount=500
        )
        payment.save()
