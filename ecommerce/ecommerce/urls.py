from django.contrib import admin
from django.urls import path
from service import views
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('', views.home, name='home'),
    path('', views.user_form, name='user_form'),
]