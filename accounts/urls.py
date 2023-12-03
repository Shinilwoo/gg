from django.urls import path
from django.contrib.auth import views as auth_view

#from polls import views
from .views import register, user_profile, user_list, select_user

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html',), name='logout'),
    path('register/', register, name='register'),
    path('user_list/', user_list, name='user_list'),
    path('select_user/', select_user, name='select_user'),
    path('user_profile/<int:user_id>/', user_profile, name='user_profile'),
]