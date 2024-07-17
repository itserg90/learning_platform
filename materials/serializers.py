from rest_framework.serializers import ModelSerializer, SerializerMethodField

from materials.models import Course, Lesson, Subscription
from materials.validators import URLValidator


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [URLValidator(field="url")]


class CourseDetailSerializer(ModelSerializer):
    number_of_lessons = SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True)

    subscription = SerializerMethodField()

    def get_number_of_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        return Subscription.objects.filter(course=course).exists()

    class Meta:
        model = Course
        fields = ("name", "number_of_lessons", "lessons", "subscription")
