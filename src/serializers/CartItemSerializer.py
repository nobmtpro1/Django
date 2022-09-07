from dataclasses import fields
from rest_framework import serializers
from ..models import CourseCategory, Course, Session,CartItem
from .DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class SessionSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"


class CourseSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CartItemSerializer(DynamicFieldsModelSerializer):
    course = CourseSerializer(many=False, read_only=True)
    session = SessionSerializer(many=False, read_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"
