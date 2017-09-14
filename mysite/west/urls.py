from django.conf.urls import url
from west import views

urlpatterns = [
    url(r'^$', views.first_page),
]