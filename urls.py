static_buildfrom django.conf.urls.defaults import *
from django.conf import settings

if settings.DEBUG:
	# Serve all local files from MEDIA_ROOT below /localmedia/
    urlpatterns = patterns('', 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
else:
    urlpatterns = patterns('',)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns += patterns('',
    
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    # (r'^about/$', 'django.views.generic.simple.direct_to_template', {'template': 'about.html'}),
    
    

)
