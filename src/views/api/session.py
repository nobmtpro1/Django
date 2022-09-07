from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch

from ...serializers.CourseCategorySerializer import CourseCategorySerializer
from ...serializers.CourseSerializer import CourseSerializer
from ...serializers.SessionSerializer import SessionSerializer
from ...serializers.CartItemSerializer import CartItemSerializer
from ...models import Session, CourseCategory, Course, CartItem


def index(request):

    # courseCategories = CourseCategory.objects.all()
    # serializer = CourseCategorySerializer(
    #     courseCategories, fields=("id", "name", "created_at", "courses","courses_with_sessions","sessions"), many=True
    # )

    # courses = Course.objects.all()
    # serializer = CourseSerializer(
    #     courses, many=True
    # )

    sessions = Session.objects.all().filter(name__startswith ="Session 1").prefetch_related("course","course_category")
    serializer = SessionSerializer(sessions, many=True)

    # cartItems = CartItem.objects.all().prefetch_related("course", "session")
    # serializer = CartItemSerializer(cartItems, many=True)

    return JsonResponse({"sessions": serializer.data}, safe=False)
