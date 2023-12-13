from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path('logout/',views.logout,name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('',views.login,name='login')]

