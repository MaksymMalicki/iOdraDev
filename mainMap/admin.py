from django.contrib import admin
from .models import Chunk, Lock, Marina, Weir

admin.site.register(Chunk)
admin.site.register(Lock)
admin.site.register(Marina)
admin.site.register(Weir)
