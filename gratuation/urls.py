from django.conf.urls import include, url
from django.contrib import admin
from myapp.views import homepage

urlpatterns = [
    # Examples:
    url(r'^admin/', admin.site.urls),

    url(r'^$', homepage),
    # url(r'^search/', include('haystack.urls')),
    url(r'^medicine/', include('myapp.urls')),

]
