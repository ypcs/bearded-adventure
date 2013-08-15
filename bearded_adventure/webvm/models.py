# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField, UUIDField

class HwConfiguration(models.Model):
    uuid = UUIDField()
    memory_size = models.PositiveIntegerField()
    cpu_count = models.PositiveIntegerField()    

class Slave(models.Model):
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User)

class MachineImage(models.Model):
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    hardware = models.ForeignKey(HwConfiguration)
    
    url = models.URLField()
    checksum = models.CharField(max_length=255)

class VirtualMachine(models.Model):
    uuid = UUIDField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    machine_image = models.ForeignKey(MachineImage)
    owner = models.ForeignKey(User)

class Snapshot(models.Model):
    uuid = UUIDField()
    vm = models.ForeignKey(VirtualMachine)
