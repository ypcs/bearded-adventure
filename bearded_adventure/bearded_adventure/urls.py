from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from webvm.api import VirtualMachineResource, SlaveResource, MachineImageResource, JobQueueResource

v1_api = Api(api_name='v1')
v1_api.register(VirtualMachineResource())
v1_api.register(SlaveResource())
v1_api.register(MachineImageResource())
v1_api.register(JobQueueResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bearded_adventure.views.home', name='home'),
    # url(r'^bearded_adventure/', include('bearded_adventure.foo.urls')),

    url(r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
