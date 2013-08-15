from django.contrib import admin
from webvm.models import Slave, MachineImage, VirtualMachine, HwConfiguration, Snapshot

admin.register(Slave)
admin.register(MachineImage)
admin.register(VirtualMachine)
admin.register(HwConfiguration)
admin.register(Snapshot)
