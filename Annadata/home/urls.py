from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [

    path('',views.index,name="index"),
    path('main',views.index,name="main"),
    path('signup',views.signup,name="signup"),
    path('login',views.Login,name="login"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path("farmDash.html",views.farmDash, name="farmDash")
]