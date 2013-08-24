# E-Uni wspace
# Copyright (c) 2013 Joshua Blake <joshbblake@gmail.com>
from csv import writer
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from euniwspace.models import ScannerLog
import datetime
from django.shortcuts import render

def scanners(request, auth, map_id, from_date, format, to_date=None):
    """Take logs between requested dates and display in csv"""
    if settings.EUNI_AUTH != auth or format not in ('csv', 'xml'):
        raise PermissionDenied 
    if not to_date:
        to_date = datetime.datetime.combine(datetime.date.today(),
                                            datetime.time.max)
    else:
        to_date = datetime.datetime.combine(datetime.datetime.strptime(
                        to_date, '%Y-%m-%d'), datetime.time.max)
        
    from_date = datetime.datetime.combine(datetime.datetime.strptime(
                        from_date, '%Y-%m-%d'), datetime.time.min)
    logs = ScannerLog.objects.filter(time__range=(from_date, to_date))\
            .filter(map_id=map_id).select_related('user__username',
                'system__name', 'sig_type__longname')
            
    if format == 'csv':
        response = HttpResponse(mimetype='text/csv')
        csv = writer(response)
        csv.writerow(('Scanner', 'Time', 'System', 'Signature ID', 'Type', 'Info',
                     'Strength'))
        for log in logs:
            try:
                longname = log.sig_type.longname
            except:
                longname = ''
            csv.writerow((log.user.username, log.time.strftime('%Y-%m-%d %H:%M'),
                         log.system.name, log.sigid, longname, 
                         log.info, log.strength))
        return response
     
    elif format == 'xml':
        return render(request, 'scanners.xml', {'logs': logs},
                      content_type='application/xml')
