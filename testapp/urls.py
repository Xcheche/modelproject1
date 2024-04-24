from django.urls import path
from .views import EmployeeInfo

urlpatterns = [
    path('',EmployeeInfo.as_view(),name='EmployeeInfo'),
]