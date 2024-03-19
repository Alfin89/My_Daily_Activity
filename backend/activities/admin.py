from django.contrib import admin
from .models import Activity


models_list = [Activity]
admin.site.register(models_list)
