from django.conf.urls import url
from .views import homepage, login, register, shopping, details,\
    news, recommend, research

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
    url(r'^shopping/([\u4E00-\u9FA5])', shopping),
    url(r'^research/([\u4E00-\u9FA5])', research),
    url(r'^details/(\d+)', details),
    url(r'^news', news),
    url(r'^recommend', recommend),
]
