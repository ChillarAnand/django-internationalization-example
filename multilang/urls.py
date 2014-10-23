from django.conf.urls import patterns, include, url
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns


from apps.data.views import about
urlpatterns = solid_i18n_patterns('',
    url(r'^main/$', about, name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
