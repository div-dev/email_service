from django.urls import path
from .views import initiateEmail

urlpatterns = [
    path('initiateEmail/', initiateEmail, name='initiateEmail'),
]
