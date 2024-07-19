# Generated by Django 5.0.6 on 2024-07-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_payment_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Наличные", "Наличные"),
                    ("Перевод на счет", "Перевод на счет"),
                ],
                help_text="Укажите тип оплаты",
                max_length=50,
                null=True,
                verbose_name="Способ оплаты",
            ),
        ),
    ]
