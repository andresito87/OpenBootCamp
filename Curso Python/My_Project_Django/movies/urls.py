from . import views
from django.conf.urls import url

from movies.views import directors

urlpatterns = [
    url(
        r'^$',
        views.movies,
        name='movies'
    ),
    url(
        r'^(?P<movie_id>\d+)/detail/$',
        views.detail,
        name='detail'
    ),
    url(
        'directors/',
        views.directors,
        name='directors'
    )
]
