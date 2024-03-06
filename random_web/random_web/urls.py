from django.contrib import admin
from django.urls import path
from generation.views import generate_random_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', generate_random_code, name='generate_random_code'),
]
