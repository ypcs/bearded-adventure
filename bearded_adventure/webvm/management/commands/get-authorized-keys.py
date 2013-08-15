import django.db

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.db import connection, transaction
from django.contrib.sites.models import Site

from webvm.models import Slave

import os

SSH_FLAGS = (
    'no-port-forwarding',
    'no-X11-forwarding',
    'no-agent-forwarding',
    'no-pty',
)

class Command(BaseCommand):
    help = ''
    
    def handle(self, *args, **kwargs):
        slaves = Slave.objects.filter(status='E')
        for s in slaves:
            print 'command="webvm-get-slave-connection %s",%s %s' % (s.uuid, ",".join(SSH_FLAGS), s.ssh_public_key)
