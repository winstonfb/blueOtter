from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
        url(r'^$', views.index, name= 'index'),
        url(r'^otter/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        ]
