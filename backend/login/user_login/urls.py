from django.urls import path
from . import views_login

app_name = 'user_login'
urlpatterns = [
    path('get/admin/data/', views_login.get_admin_password, name='get_admin_password'),
    path('get/customer/data/', views_login.get_customer_password, name='get_admin_password'),
]


