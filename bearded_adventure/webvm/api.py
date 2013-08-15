from tastypie.resources import ModelResource
from webvm.models import Slave, Snapshot, VirtualMachine, MachineImage, HwConfiguration


class VirtualMachineResource(ModelResource):
    class Meta:
        queryset = VirtualMachine.objects.all()
        resource_name = 'virtualmachine'

class SlaveResource(ModelResource):
    class Meta:
        queryset = Slave.objects.all()
        resource_name = 'slave'

class MachineImageResource(ModelResource):
    class Meta:
        queryset = MachineImage.objects.all()
        resource_name = 'machine-image'
