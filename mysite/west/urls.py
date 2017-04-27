from django.conf.urls import url
from west.views import first_page

urlpatterns = [
    url(r'^$',first_page),
]