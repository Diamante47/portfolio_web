from django.urls import path 
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('portfolio-details/<str:proyecto>/', views.portfolio_details, name='portfolio_details'),
    path('service-details/', views.service_details, name='service_details'),
    path('starter-page/', views.starter_page, name='starter_page'),
]