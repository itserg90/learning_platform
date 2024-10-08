# Generated by Django 5.0.6 on 2024-07-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_payment_payment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите ID сессии",
                max_length=255,
                null=True,
                verbose_name="ID сессии",
            ),
        ),
    ]
