from django.conf.urls import url

from core.views import family_details, location_details

urlpatterns = [
    url(r'^family_details/$', family_details),
    url(r'^location/(?P<pincode>[0-9]{6})/$', location_details)
]
