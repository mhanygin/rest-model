from django.conf.urls import url
from .view import change_model, new_model

urlpatterns = [url(r'^(?P<model>[a-zA-Z]+)/(?P<id>[0-9]+)$', change_model),
               url(r'^(?P<model>[a-zA-Z]+)$', new_model)]
