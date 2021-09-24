from main.views import home, teacher_login
from django.urls import path
from main.views import teacher_login, student_login, admin_login, request_attendance, teacher_register, student_register, give_attendance, handlelogout

urlpatterns = [
    path('',home,name="home"),
    path('teacher_login',teacher_login, name="teacher_login"),
    path('student_login',student_login, name="student_login"),
    path('admin_login',admin_login, name="admin_login"),
    path('teacher_register',teacher_register, name="teacher_register"),
    path('student_register',student_register, name="student_register"),
    path('give_attendance/<user_id>',give_attendance, name="give_attendance"),
    path('request_attendance/<user_id>',request_attendance, name="request_attendance"),
    path('logout/',handlelogout, name="logout")
]
