from django.contrib import admin
from .models import Blog, Article, Equipment, ResearchLog

# Register your models here.
admin.site.register(Blog)
admin.site.register(Article)
@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'serial_number', 'date_acquired')
    search_fields = ('name', 'type', 'serial_number')
@admin.register(ResearchLog)
class ResearchLogAdmin(admin.ModelAdmin):
    list_display = ('experiment_name', 'researcher', 'date')
    search_fields = ('experiment_name', 'researcher')
