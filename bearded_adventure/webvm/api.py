from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from webvm.models import Slave, Snapshot, VirtualMachine, MachineImage, HwConfiguration, JobQueueItem
from bearded_adventure.common import CamelCaseJSONSerializer

class VirtualMachineResource(ModelResource):
    class Meta:
        queryset = VirtualMachine.objects.all()
        resource_name = 'virtualmachine'
        serializer = CamelCaseJSONSerializer()

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
#        detail_uri_name = 'uuid'
    
#    def prepend_urls(self):
#        return [url(r'^(?P<resource_name>%s)/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', self._meta.resource_name, self.wrap_view('dispatch_detail'), name='api_dispatch_detail')]

class MachineImageResource(ModelResource):
    class Meta:
        queryset = MachineImage.objects.all()
        resource_name = 'machine-image'
        serializer = CamelCaseJSONSerializer()

class JobQueueResource(ModelResource):
    class Meta:
        queryset = JobQueueItem.objects.all().order_by('-priority', 'created')
        resource_name = 'queue'
        serializer = CamelCaseJSONSerializer()
        excludes = ['id',]