from django.contrib import admin

from materials.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "course",
    )
    readonly_fields = ["user", "course"]
