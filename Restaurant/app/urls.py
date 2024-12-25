from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('food',views.food,name='food'),
    path('veg',views.veg,name='veg'),
    path('nonveg',views.nonveg,name='nonveg'),
    path('breakfast',views.breakfast,name='breakfast'),
    path('veglunch',views.veglunch,name='veglunch'),
    path('vegdinner',views.vegdinner,name='vegdinner'),
    path('nonlunch',views.nonlunch,name='nonlunch'),
    path('nondinner', views.nondinner, name='nondinner'),
    path('chefs', views.chefs, name='chefs'),
    path('cfood',views.cfood,name='cfood'),
    path('lunch',views.lunch,name='lunch'),
    path('dinner',views.dinner,name='dinner'),
    path('bfast',views.bfast,name='bfast')

]