import django.db

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import connection, transaction
from django.contrib.sites.models import Site

from webvm.models import Slave

import os

class Command(BaseCommand):
    help = ''
    
    def handle(self, *args, **kwargs):
        slaves = Slave.objects.filter(status='E')
        for s in slaves:
            print '%s' % s.ssh_public_key
