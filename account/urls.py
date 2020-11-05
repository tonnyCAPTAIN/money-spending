from django.urls import path

from .views import home, register, login, salary, about

urlpatterns = [
    
    
    path('', home, name="home"),
    path('register/',register, name="register"),
    path('login/', login, name="login"),
    path('salary/', salary, name="salary"),
    path('about/', about, name="about"),
]
