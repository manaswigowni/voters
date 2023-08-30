"""
URL configuration for tofass1 project.

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

from tofassignment1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('distr_login/', views.distr_login, name='distr_login'),
    path('consti_login/', views.consti_login, name='consti_login'),
    path('voterview/', views.voterview, name='voterview'),
    path('districtview/', views.districtview, name='districtview'),
    path('voterslist/', views.voters_list, name='voters_list'),
    path('view_voter_details/<str:voter_id>/', views.view_voter_details, name='view_voter_details'),
    path('voterslist/update_voter/<str:voter_id>/', views.update_voter, name='update_voter'),
    path('edit_voter/<str:voter_id>/', views.edit, name='edit_voter'),

]
