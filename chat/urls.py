from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    path("regi_ptn/", views.regi_ptn, name="regi_ptn"),
    path('', views.chat, name='chat'),
    path('check_ptn/', views.check_ptn, name='check_ptn'),
]
