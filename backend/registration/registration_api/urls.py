from django.contrib import admin
from django.urls import path
from registration_api.views import RegistrationCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/register/', RegistrationCreateView.as_view(), name='register'),
]

