from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import ServiceType

class ServiceTypeView(View):
    def get(self, request):
        serviceType = ServiceType.objects.all()
        # return  HttpResponse(':)', status=200)
        return render(request, 'netbox_services_types/service_type.html', {
            'serviceType': serviceType,
        })
