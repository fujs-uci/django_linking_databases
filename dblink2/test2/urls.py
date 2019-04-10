from django.urls import path
from . import views

app_name = 'test2'
urlpatterns = [
    path('', views.test2_home, name='test2_home'),
    path('<int:user_id>/object-manage/', views.test2_object_manage, name='test2_object_manage'),
]