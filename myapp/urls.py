from django.urls import path
from . import views

urlpatterns=[
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('home/', views.home, name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('meeting/',views.meeting,name='meeting'),
    path('logout/',views.logout,name="logout"),
    path('joinmeeting/',views.joinmeeting,name="joinmeeting"),
]