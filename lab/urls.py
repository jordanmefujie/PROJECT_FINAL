from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lab_test/<int:id>/', views.lab_test_detail, name='lab_test_detail'),
    path('protocol/<int:id>/', views.protocol_detail, name='protocol_detail'),
]
