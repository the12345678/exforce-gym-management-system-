from django.urls import path
from . import views,customers_views


app_name = 'supplement'
urlpatterns = [
    path('product/data/', views.save_gym_supplement_data, name='save_gym_supplement_data'),
    path('get/product_data/', views.send_supplement_data, name='save_gym_supplement_data'), 
    path('update/product/data/', views.update_gym_supplement_data, name='update_gym_supplement_data'),      
    path('send/product_data/', customers_views.save_change_table_data, name='save_customer_table_data'), 
    
]