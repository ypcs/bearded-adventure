# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField, UUIDField

def get_id(object):
    return "%s-%s" % (object.prefix, object.uuid)

class HwConfiguration(models.Model):
    prefix = 'hw'
    uuid = UUIDField()
    memory_size = models.PositiveIntegerField()
    cpu_count = models.PositiveIntegerField()    

    def __str__(self):
        return "%s (cpu: %d, mem: %dMB)" % (get_id(self), self.cpu_count, self.memory_size)

class Slave(models.Model):
    SLAVE_STATUSES = (
        ('E', 'Enabled'),
        ('D', 'Disabled'),
        ('B', 'Banned'),
    )
    prefix = 'sl'
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User)

    status = models.CharField(max_length=2, choices=SLAVE_STATUSES)
    
    ssh_public_key = models.TextField(blank=True,null=True, verbose_name='SSH Public Key')
    
    def __str__(self):
        return "%s (%s, owner: %s)" % (get_id(self), self.name, self.owner)

class MachineImage(models.Model):
    prefix = 'mi'
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    hardware = models.ForeignKey(HwConfiguration)
    
    url = models.URLField()
    checksum = models.CharField(max_length=255)

    def __str__(self):
        return "MI %s (%s, %s)" % (get_id(self), self.name, self.hardware)

class VirtualMachine(models.Model):
    prefix = 'vm'
    uuid = UUIDField()
    slave = models.ForeignKey(Slave, blank=True, null=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    machine_image = models.ForeignKey(MachineImage)
    owner = models.ForeignKey(User)

    def __str__(self):
        return "VM %s" % self.uuid

class Snapshot(models.Model):
    prefix = 's'
    uuid = UUIDField()
    vm = models.ForeignKey(VirtualMachine)
    
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def __str__(self):
        return "Snapshot %s" % self.uuid

class JobQueueItem(models.Model):
    prefix = 'JQ'
    JOBQUEUE_STATUSES = (
        ('W', 'Waiting'),
        ('R', 'Running'),
        ('C', 'Completed'),
        ('F', 'Failure'),
    )
    uuid = UUIDField()
    vm = models.OneToOneField(VirtualMachine)
    
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    status = models.CharField(max_length=2, choices=JOBQUEUE_STATUSES)
    priority = models.IntegerField(default=0)

    def update_status(self, new_status):
        # TODO: Check that new_status is a valid status
        self.status = new_status
        self.save()
    
    def __str__(self):
        return "%s (%s) (p: %d)" % (get_id(self), self.vm, self.priority)
