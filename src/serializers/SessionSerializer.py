from ..models import CourseCategory, Course, Session
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class CourseCategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class CourseSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class SessionSerializer(DynamicFieldsModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    course_category = CourseCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Session
        fields = "__all__"
