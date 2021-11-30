from django.urls import path
from .views import landing_view, map_view, chunk_view, messages_view, locks_table_view, lock_details, marina_details, weir_details, search, water_safety_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainMap'

urlpatterns = [
    path('', landing_view, name="landing"),
    path('map/', map_view, name="map"),
    path('komunikaty/', messages_view, name="komunikaty"),
    path('sluzy/', locks_table_view, name="sluzy"),
    path('bezpieczenstwo/', water_safety_view, name="water_safety"),
    path('sluza/<str:slug>', lock_details, name="sluza_details"),
    path('marina/<str:slug>', marina_details, name="marina_details"),
    path('jaz/<str:slug>', weir_details, name="jaz_details"),
    path('map/search/', search, name="search"),
    path('map/<str:slug>/', chunk_view, name="chunk"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
