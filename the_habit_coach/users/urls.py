"""
URL configuration for recommendation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import register, login_view, dashboard, logout_user, home, HabitListView, HabitCreateView, HabitDetailView, HabitUpdateView, HabitDeleteView, HabitLogCreateView

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', HabitListView.as_view(), name='dashboard'),
    path('dashboard/habit/<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('dashboard/habit/<int:pk>/update/', HabitUpdateView.as_view(), name='habit-update'),
    path('dashboard/habit/<int:pk>/delete/', HabitDeleteView.as_view(), name='habit-delete'),
    path('dashboard/habit/<int:pk>/log/', HabitLogCreateView.as_view(), name='habit-log'),
    path('dashboard/habit/new', HabitCreateView.as_view(), name='habit-create'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]
