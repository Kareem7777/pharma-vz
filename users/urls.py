from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView , LogoutView
urlpatterns = [


    path('', indexview , name="start"),

    #path('dashboard/', dashboardView,name="dashboard"),
    path('login/', LoginView.as_view(),name="login_url"),
    path('register/',registerView ,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='start'),name="logout_url" ),



]
