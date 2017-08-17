from django.conf.urls import url

from core.views import family_details, location_details

urlpatterns = [
    url(r'^family_details/(?P<family_id>[A-Z]{7})/$', family_details),
    url(r'^location/(?P<pincode>[0-9]{6})/$', location_details)
]
