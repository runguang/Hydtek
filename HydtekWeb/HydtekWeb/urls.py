from django.conf.urls import patterns, include, url
from hello import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # try stuff
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
