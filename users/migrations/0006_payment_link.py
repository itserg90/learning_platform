# Generated by Django 5.0.6 on 2024-07-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_payment_session_id_alter_payment_course_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
    ]
