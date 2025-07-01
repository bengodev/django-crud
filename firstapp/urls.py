from django.urls import path
from . import views


urlpatterns = [
    path('function', views.hello_app),
    path('class', views.HelloWorld.as_view()),
    path('reservation', views.home)
]
