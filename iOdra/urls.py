from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('telephones.urls', namespace="contactApp")),
    path('', include('mainMap.urls', namespace="mainMap")),
]
