from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'gratuation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'urls/', include('myapp.urls'))
]