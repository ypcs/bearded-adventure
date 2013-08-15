from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from webvm.api import VirtualMachineResource

vm_resource = VirtualMachineResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bearded_adventure.views.home', name='home'),
    # url(r'^bearded_adventure/', include('bearded_adventure.foo.urls')),

    url(r'^api/', include(vm_resource.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
