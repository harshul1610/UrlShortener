__author__ = 'h_hack'
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index, name='index' ),
    url(r'^(?P<shortkey>[0-9a-zA-Z])', views.redirectview, name='redirect')
]