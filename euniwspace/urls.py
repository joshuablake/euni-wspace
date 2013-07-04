from django.conf.urls import patterns

BASE_SCAN_URL = r'^scanners/(?P<auth>[^/]+)/(?P<map_id>\d+)/(?P<from_date>\d{4}-\d{2}-\d{2})'

urlpatterns = patterns('euniwspace.views',
    (BASE_SCAN_URL + '\.(?P<format>[a-z]{3})/$', 'scanners'),
    (BASE_SCAN_URL + '/(?P<to_date>\d{4}-\d{2}-\d{2})\.(?P<format>[a-z]{3})/$', 'scanners')
)