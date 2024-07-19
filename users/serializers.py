import stripe
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from users.models import User, Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class PaymentStatusSerializer(ModelSerializer):
    status = SerializerMethodField()

    def get_status(self, obj):
        session = stripe.checkout.Session.retrieve(obj.session_id)
        return session.status

    class Meta:
        model = Payment
        fields = (
            "session_id",
            "user",
            "course",
            "lesson",
            "payment_amount",
            "link",
            "status",
        )


class UserSerializer(ModelSerializer):
    payments = PaymentSerializer(source="payment_set", many=True, read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class UserRetrieveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", "email", "city")
