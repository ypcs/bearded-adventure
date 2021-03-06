from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from webvm.models import Slave, Snapshot, VirtualMachine, MachineImage, HwConfiguration, JobQueueItem
from bearded_adventure.common import CamelCaseJSONSerializer
from tastypie import fields
from tastypie.authentication import ApiKeyAuthentication

class SlaveResource(ModelResource):
    class Meta:
        queryset = Slave.objects.all()
        resource_name = 'slave'
        excludes = [
            'id',
            'ssh_public_key',
        ]
        filtering = {
            'uuid': ALL,
        }
        serializer = CamelCaseJSONSerializer()
        authentication = ApiKeyAuthentication()
#        detail_uri_name = 'uuid'
    
#    def prepend_urls(self):
#        return [url(r'^(?P<resource_name>%s)/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$' % self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail')]

class MachineImageResource(ModelResource):
    class Meta:
        queryset = MachineImage.objects.all()
        resource_name = 'machine-image'
        serializer = CamelCaseJSONSerializer()
        excludes = ['id',]
        authentication = ApiKeyAuthentication()


class VirtualMachineResource(ModelResource):
    machine_image = fields.ForeignKey(MachineImageResource, 'machine_image')
    class Meta:
        queryset = VirtualMachine.objects.all()
        resource_name = 'virtual_machine'
        serializer = CamelCaseJSONSerializer()
        authentication = ApiKeyAuthentication()

class JobQueueResource(ModelResource):
    virtual_machine = fields.ForeignKey(VirtualMachineResource, 'vm')
    class Meta:
        queryset = JobQueueItem.objects.all().order_by('-priority', 'created')
        resource_name = 'queue'
        serializer = CamelCaseJSONSerializer()
        excludes = ['id',]
        authentication = ApiKeyAuthentication()
