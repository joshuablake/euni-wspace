# E-Uni wspace
# Copyright (c) 2013 Joshua Blake <joshbblake@gmail.com>
from Map.models import System, SignatureType, Map
from Map.signals import signature_update
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.dispatch.dispatcher import receiver

class ScannerLog(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField()
    system = models.ForeignKey(System)
    sigid = models.CharField(max_length=7)
    sig_type = models.ForeignKey(SignatureType, null=True)
    info = models.CharField(max_length=65, null=True)
    strength = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    map = models.ForeignKey(Map)

@receiver(signature_update)
def add_log(**kwargs):
    signature = kwargs['sender']
    try:
        signal_strength = kwargs['signal_strength']
    except KeyError:
        signal_strength = None
    ScannerLog(user=kwargs['user'], time=datetime.now(), system=signature.system,
        sigid=signature.sigid, sig_type=signature.sigtype,
        info=signature.info, strength=signal_strength, map=kwargs['map']).save()
