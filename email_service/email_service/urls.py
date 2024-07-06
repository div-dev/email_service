from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('',include("mail.urls")),
    path('admin/', admin.site.urls),
]
