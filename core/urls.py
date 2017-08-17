from django.conf.urls import url

from core.views import family_details

urlpatterns = [
    url(r'^family_details/$', family_details),
]
