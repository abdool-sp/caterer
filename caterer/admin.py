from django.contrib import admin

# Register your models here.
from .models import Service,Caterer

admin.site.register(Caterer)
admin.site.register(Service)