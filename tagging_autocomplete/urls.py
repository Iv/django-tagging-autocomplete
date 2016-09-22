from django.conf.urls import *
from tagging_autocomplete.views import list_tags

urlpatterns = [
    # 'tagging_autocomplete.views',
    url(r'^list$', list_tags, name='tagging_autocomplete-list'),
]
