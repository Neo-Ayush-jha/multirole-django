from django.contrib import admin
from django.urls import path
from rms.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/student/register/',StudentSingupView.as_view(),name="student_register"),
    path('account/teacher/register/',TeacherSingupView.as_view(),name="teacher_register"),
    path('',HomePageView.as_view(),name="home"),
    path('singup/',SingUp.as_view(),name="singup"),
    path('teacher/',Teacher.as_view(),name="teacher"),
    path('student/',Student.as_view(),name="student"),
]
