from django.urls import path
from . import views_coachattendance, views_memberattendance


app_name = 'attendance'
urlpatterns = [
    path('memberdata/', views_memberattendance.save_member_attendance_data, name='save_member_attendance_data'),
    path('coachdata/', views_coachattendance.save_coach_attendance_data, name='save_coach_attendance_data'),
]

