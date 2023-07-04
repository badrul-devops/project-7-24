from django.contrib import admin
from django.urls import path
from service import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('user-form/', views.user_form, name='user_form'),
    path('admin-portal/', views.admin_portal, name='admin_portal'),
    path('login/' ,views.userlogin, name='user_login'),
    path ('register/', views.userregister, name='user_register'),
]