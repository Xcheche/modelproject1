from django.shortcuts import render
from testapp.models import Employee #model import
from django.views.generic import  TemplateView # import for class based view
# Create your views here.
class EmployeeInfo(TemplateView):
    employees = Employee.objects.all()
    template_name = 'testapp/results.html'

    def get_context_data(self):
        return {'employees': Employee.objects.all()}