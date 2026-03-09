from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accountability/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('update/', views.daily_update_view, name='daily_update'),
    path('add-partner/', views.add_partner, name='add_partner'),
    path('connect-partner/<int:user_id>/', views.connect_partner, name='connect_partner'),
    path('complete-goal/<int:goal_id>/', views.complete_goal, name='complete_goal'),
]
