from django.urls import path
from . import views_coach,views_member,views_admin,views_customer


app_name = 'registration'
urlpatterns = [
    path('member/data/', views_member.save_member_registration_data, name='save_member_registration_data'),  
    path('coach/data/', views_coach.save_coach_registration_data, name='save_coach_registration_data'),
    path('delete/admin/data/', views_admin.delete_admin_registration_data, name='delete_admin_registration_data'),
   
    path('admin/data/', views_admin.save_administrator_data, name='save_administrator_registration_data'), 
    path('customer/data/',views_customer.save_customer_data,name='save_customer_data'),
    path('coach-names/', views_member.get_coach_names, name='get_coach_names'),
]

