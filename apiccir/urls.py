
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('inscription/',views.inscription, name="inscription"),
    path('connexion/',views.connexion, name="connexion"),
    path('contact/',views.contact, name="contact"),
    path('tableaudebord/',views.tableaudebord, name="tableaudebord"),
]
