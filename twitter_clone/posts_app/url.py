from django.urls import path

from . import views

app_name = 'posts_app'

urlpatterns =[
    path('', views.first),
    path('group/<slug:slug>/', views.second, name='group_list')
]