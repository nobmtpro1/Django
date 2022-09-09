from .BaseRepository import BaseRepository
from src.models.Course import Course
from ..models import CourseCategory, Course, Session, UserClient
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class CourseCategorySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"


class SessionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class UserClientSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = UserClient
        fields = "__all__"


class CourseSerializer(DynamicFieldsModelSerializer):
    sessions = SessionSerializer(source="session_set", many=True, read_only=True)
    course_category = CourseCategorySerializer(many=False, read_only=True)
    user = UserClientSerializer(source="userclient_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class CourseRepository(BaseRepository):
    def __init__(self):
        self.model = Course

    def getAllWithAllRelatedSerialize(self):
        courses = self.model.objects.all()
        return CourseSerializer(courses, many=True)
