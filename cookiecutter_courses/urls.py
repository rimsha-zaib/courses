
from django.urls import path
from django.contrib import admin

from . import views  # Import your views module
from cookiecutter_courses.views import get_courses, CourseListAPIView

urlpatterns = [
    path('v1/list/', CourseListAPIView.as_view(), name='course_list')
]
#helllo
