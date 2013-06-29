# E-Uni wspace
# Copyright (c) 2013 Joshua Blake <joshbblake@gmail.com>
from csv import writer
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from euniwspace.models import ScannerLog
import datetime

def CSV_scanners(request, auth, map_id, from_date, to_date=None):
    if settings.EUNI_AUTH != auth: raise PermissionDenied 
    if not to_date:
        to_date = datetime.date.today()
    else:
        to_date = datetime.datetime.combine(datetime.datetime.strptime(
                        to_date, '%Y-%m-%d'), datetime.time.max)
        
    from_date = datetime.datetime.combine(datetime.datetime.strptime(
                        from_date, '%Y-%m-%d'), datetime.time.min)
    response = HttpResponse(mimetype='text/csv')
    logs = ScannerLog.objects.filter(time__range=(from_date, to_date))\
            .filter(map_id=map_id).select_related('user__username',
                'system__name', 'sig_type__longname')
    csv = writer(response)
    csv.writerow(('Scanner', 'Time', 'System', 'Signature ID', 'Type', 'Info',
                 'Strength'))
    for log in logs:
        csv.writerow((log.user.username, log.time.strftime('%Y-%m-%d %H:%M'),
                     log.system.name, log.sigid, log.sig_type.longname, 
                     log.info, log.strength))
    return response
    