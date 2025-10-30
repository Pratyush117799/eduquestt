from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('features/', views.features_page, name='features'),
    path('lecture/', views.lecture_page, name='lecture'),
    path('signup_teacher/', views.signup_teacher, name='signup_teacher'),
    path('login_teacher/', views.login_teacher, name='login_teacher'),
    path('dashboard_teacher/', views.dashboard_teacher, name='dashboard_teacher'),
    
]
