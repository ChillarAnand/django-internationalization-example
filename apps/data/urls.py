from django.conf.urls import patterns, include, url
from solid_i18n.urls import solid_i18n_patterns

from .views import about

urlpatterns = solid_i18n_patterns('',
    url(r'^main/$', 'about.view', name='about'),
)
