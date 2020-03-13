from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import homepage

urlpatterns = [
    # Examples:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', homepage),
    url(r'^medicine/', include('myapp.urls')),
]
