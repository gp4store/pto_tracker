from django.contrib import admin
from .models import pto_type, pto_request


admin.site.register(pto_request)
admin.site.register(pto_type)
# Register your models here.
