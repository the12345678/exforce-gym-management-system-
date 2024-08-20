from django.urls import path
from . import views_coachpayment, views_memberpayment

app_name = 'payment'
urlpatterns = [
    path('memberdata/', views_memberpayment.save_member_payment_data, name='save_member_attendance_data'),
    path('sendsalary/', views_memberpayment.calculate_fee, name='calculate_fee'),
    path('coachdata/', views_coachpayment.save_coach_payment_data, name='save_coach_attendance_data'),
]
