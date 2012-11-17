from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gerenciador.views.home', name='home'),
    # url(r'^gerenciador/', include('gerenciador.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^$', 'agenda.views.lista'),
    (r'^adiciona/$', 'agenda.views.adiciona'),
    (r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'),

    (r'^login/$', 'django.contrib.auth.views.login',
                    {'template_name': 'login.html' }),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login',
                    {'login_url': '/login/'}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
