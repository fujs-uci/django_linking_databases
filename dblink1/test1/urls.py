from django.urls import path
from . import views

app_name = 'test1'
urlpatterns = [
    path('', views.test1_home, name='test1_home'),
    path('signup/', views.test1_signup, name='test1_signup'),
]
