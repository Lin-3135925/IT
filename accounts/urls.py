from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # custom signup view
    path('signup/', views.signup_view, name='signup'),
    
    # using django's built-in auth views
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='browse'), name='logout'),
]