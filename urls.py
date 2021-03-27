from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name = 'index'),
    path("signup/",views.signup,name = "signup"),
    path("login/",views.login,name = "login"),
    path("fac/",views.fac,name = "fac"),
    path("login/getdetails/",views.logined,name = 'getdetails'),
]
