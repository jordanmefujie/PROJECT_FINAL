from django.urls import path
from .views import LabTestListView, LabTestDetailView, LabTestCreateView, LabTestUpdateView, LabTestDeleteView

urlpatterns = [
    path('', LabTestListView.as_view(), name='test_list'),
    path('test/<int:pk>/', LabTestDetailView.as_view(), name='test_detail'),
    path('test/new/', LabTestCreateView.as_view(), name='test_create'),
    path('test/<int:pk>/edit/', LabTestUpdateView.as_view(), name='test_update'),
    path('test/<int:pk>/delete/', LabTestDeleteView.as_view(), name='test_delete'),
]
