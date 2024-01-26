from django.urls import path
from partyat import views


urlpatterns =[
    path("",views.HomePage,name="index_urls.py_partyat"),
    path("signup",views.SignUpPage,name="SignUpPage"),
    path("login",views.LogInPage,name="login"),
    path("index",views.index,name="index"),
    path("home",views.HomePage,name="HomePage"),
    path("forgotpassword",views.ForgotPassword,name="forgotPassword"),
    path("booking",views.BookingTable,name="BookingTable"),


]