from django.urls import path, include
from . import views


app_name = "users"
urlpatterns = [
    path('', include('main.urls')),
    path("register/", views.register, name='register'),
    path('login/', views.sign_in, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.sign_out, name='logout'),
]