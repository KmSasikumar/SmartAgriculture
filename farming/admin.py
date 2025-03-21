from django.contrib import admin
from .models import calculate_yeild, crop_productions

# Register your models here.
admin.site.register(calculate_yeild)
admin.site.register(crop_productions)
