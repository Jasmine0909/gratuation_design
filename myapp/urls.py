from django.conf.urls import url
from .views import homepage, login, register, shopping, details, news, recommend

# urlpatterns = [
#     url(r'^index/(\d+)', paginator_index),
#     url(r'^homepage', homepage),
#     url(r'^detail/(\d+)', detail),
#     url(r'^login_redict/', login_redict),
#     url(r'^register/', register),
#     url(r'^photo/', photo),
#     url(r'^send/', send),
#     url(r'^post/', new_post),
# ]

urlpatterns = [
    url(r'^homepage', homepage),
    url(r'^login', login),
    url(r'^register', register),
    url(r'^shopping', shopping),
    url(r'^details', details),
    url(r'^news', news),
    url(r'^recommend', recommend),
]
