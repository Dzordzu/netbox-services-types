from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth.mixins import PermissionRequiredMixin
from utilities.views import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import (
    SoftwareProviderFilter,
    LicencesFilter
)
from .forms import (
    SoftwareProviderFilterForm,
    LicencesFilterForm,
    SoftwareProviderForm
)
from .models import (
    SoftwareProvider,
    Licence
)
from .tables import (
    SoftwareProviderTable,
    LicenceTable
)

from .utilities.views import CRUDViewGenerator

####
## SoftwareProvider
####

software_provider_generator = CRUDViewGenerator("SoftwareProvider")

SoftwareProviderListView = software_provider_generator.list()
SoftwareProviderCreateView = software_provider_generator.create()

class SoftwareProviderBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """ Remove multiple Software Providers """
    permission_required = 'netbox_licences.delete_softwareprovider'
    queryset = SoftwareProvider.objects.all()
    filterset = SoftwareProviderFilter
    table = SoftwareProviderTable
    default_return_url = "plugins:netbox_licences:software_providers_list"

class SoftwareProviderEditView(PermissionRequiredMixin, ObjectEditView):
   """ Edit existing Software Provider """
   permission_required = 'netbox_licences.edit_softwareprovider'
   queryset = SoftwareProvider.objects.all()
   model = SoftwareProvider




class LicenceListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'netbox_licences.view_licence'
    queryset = Licence.objects.all()
    filterset = LicencesFilter
    filterset_form = LicencesFilterForm
    table = LicenceTable
    template_name = "netbox_licences/licences_list.html"
