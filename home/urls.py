from django.urls import path
from home import views

urlpatterns = [
    path('', views.welcome_page, name='welcome'),
    # Other URL patterns for your application
]
