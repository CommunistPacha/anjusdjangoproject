from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search_view, name='search'),
    path('profile/', views.profile_view, name='profile'),
    path('about/', views.about_view, name='about'),
    path('courses/', views.courses_view, name='courses'),
    path('teachers/', views.teachers_view, name='teachers'),
    path('contact/', views.contact_view, name='contact'),
    path('home/', views.home_view, name='home'),
    path('', views.home_view, name='home'),
]
