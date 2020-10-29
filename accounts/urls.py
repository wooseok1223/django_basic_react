from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
# app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(),
    #      name='password_change'),
    path('password_change/', views.password_change, name='password_change'),
    path('signup/', views.signup, name='signup'),
    path('edit/', views.profile_edit, name='profile_edit'),
]