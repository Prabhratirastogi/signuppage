from django.urls import path
from.import views

urlpatterns = [
    path("",views.index,name="patientHome"),
    path("home", views.home,name="home"),
    path("about",views.about,name="AboutUs"),
    path("contact",views.contact,name="ContactUs"),
    path("signup", views.signup, name="signup"),
    path("login", views.login,name="login"),
    path("logout", views.logout, name="logout"),
]
