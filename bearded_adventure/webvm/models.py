# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField, UUIDField

class HwConfiguration(models.Model):
    __prefix = 'hw'
    uuid = UUIDField()
    memory_size = models.PositiveIntegerField()
    cpu_count = models.PositiveIntegerField()    

    def get_id(self):
        return "%s%s" % (self.__prefix, self.uuid)

    def __str__(self):
        return "%s (cpu: %d, mem: %dMB)" % (self.get_id(), self.cpu_count, self.memory_size)

class Slave(models.Model):
    __prefix = 'sl'
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User)
    
    def get_id(self):
        return "%s%s" % (self.__prefix, self.uuid)
    
    def __str__(self):
        return "%s (%s, owner: %s)" % (self.get_id(), self.name, self.owner)

class MachineImage(models.Model):
    __prefix = 'mi'
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    hardware = models.ForeignKey(HwConfiguration)
    
    url = models.URLField()
    checksum = models.CharField(max_length=255)

    def get_id(self):
        return "%s%s" % (self.__prefix, self.uuid)
    
    def __str__(self):
        return "MI %s (%s, %s)" % (self.get_id(), self.name, self.hardware)

class VirtualMachine(models.Model):
    __prefix = 'vm'
    uuid = UUIDField()
    slave = models.ForeignKey(Slave, blank=True, null=True)
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    machine_image = models.ForeignKey(MachineImage)
    owner = models.ForeignKey(User)

    def get_id(self):
        return "%s%s" % (self.__prefix, self.uuid)

    def __str__(self):
        return "VM %s" % self.uuid

class Snapshot(models.Model):
    __prefix = 's'
    uuid = UUIDField()
    vm = models.ForeignKey(VirtualMachine)
    
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()

    def get_id(self):
        return "%s%s" % (self.__prefix, self.uuid)

    def __str__(self):
        return "Snapshot %s" % self.uuid
