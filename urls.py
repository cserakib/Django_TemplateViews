from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.Home_View.as_view(), name= 'home'),
    path('about/',views.About_View.as_view(), name='about'),
    
