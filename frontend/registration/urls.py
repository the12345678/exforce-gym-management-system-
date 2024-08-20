from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('data/', views.save_registration_data, name='save_registration_data'),
]