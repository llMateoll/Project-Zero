from django.contrib import admin
from .models import Level

# Register your models here.
@admin.register(Level)
class LevelsAdmin(admin.ModelAdmin):
    list_display = ("level","price", "reference")