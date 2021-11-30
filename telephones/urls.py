from django.urls import path, include
from .views import contact_view
from django.conf import settings
from django.conf.urls.static import static

app_name = 'contactApp'

urlpatterns = [
    path('', contact_view, name="contact"),
]