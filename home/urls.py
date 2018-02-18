from django.conf.urls import url
from home.views import HomeView
from home.views import change_friends

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$',
        change_friends, name='change_friends')
]
