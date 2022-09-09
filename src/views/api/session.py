from pprint import pprint
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch

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


    # cartItems = CartItem.objects.all().prefetch_related("course", "session")
    # serializer = CartItemSerializer(cartItems, many=True)

    return JsonResponse({"sessions": ""}, safe=False)
