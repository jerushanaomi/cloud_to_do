from django.contrib import admin
from django.urls import path, include
from todo.views import home, addTodo, deleteTodo, editTodo, about
from django.contrib.auth import views as auth_views
from users import views as users_views
from django.urls import include
from django.conf import settings
from django.urls import re_path
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include('home.urls'),name='welcome'),
    path("home/", home, name="home"),
    path("users/", include('users.urls')),

    path("login/", auth_views.LoginView.as_view(template_name='users/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('about/', about, name='about'),
    path("addTodo/", addTodo, name="addTodo"),
    path("delete/<int:item_id>/", deleteTodo, name="addTodo"),
    path("edit/<int:item_id>/", editTodo, name="editTodo"),
    re_path(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]


"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
