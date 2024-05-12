from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home,name='home'),
    path('home/',views.Home,name='home'),
    path('heart/',views.Heart,name='heart'),
    path('Departments/liver/', views.Liver, name='liver'),
    path('Departments/diabetes/', views.Diabetes, name='diabetes'),
    path('Departments/heart/', views.Heart, name='heart'),
    path('Departments/cancer/', views.Cancer, name='cancer'),
   # path('diabetes/',views.Welcome,name='diabetes'),
    path('cancer/',views.Cancer,name='cancer'),
    # path('user',views.User, name='User'),
    path('Departments/liver/user/',views.User,name='user'),
    path('about/',views.About,name='about'),
    path('Departments/',views.Dept,name='dept'),
    path('Contacts/',views.Cont,name='cont'),
]
