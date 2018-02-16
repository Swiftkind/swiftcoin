from django.urls import path, re_path
from .views import User


urlpatterns = [
    path('info/', User.as_view({'get': 'status'}), name="status"),
]