
from django.urls import path
from .views_notices import save_noticeinput_data,get_notice_data,update_notice_data

app_name = 'notices'
urlpatterns = [
    path('notice_data/', save_noticeinput_data, name='save_noticeinput_data'),
    path('get_notice_data/', get_notice_data, name='get_notice_data'),
    path('update/data/',update_notice_data , name='update_notice_data'),
]

