from tastypie.resources import ModelResource
from webvm.models import Slave, Snapshot, VirtualMachine, MachineImage, HwConfiguration


class VirtualMachineResource(ModelResource):
    class Meta:
        queryset = VirtualMachine.objects.all()
        resource_name = 'virtualmachine'


