from django.contrib import admin
from webvm.models import Slave, MachineImage, VirtualMachine, HwConfiguration, Snapshot

admin.site.register(Slave)
admin.site.register(MachineImage)
admin.site.register(VirtualMachine)
admin.site.register(HwConfiguration)
admin.site.register(Snapshot)
