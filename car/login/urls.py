from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'login' 
urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^login/$', views.user_login, name='user_login'),
    path('logout/', views.signout, name="logout")
]
