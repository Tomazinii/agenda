from django.contrib import admin

from .models import Agenda
# Register your models here.

@admin.register(Agenda)
class AgendaModel(admin.ModelAdmin):
    list_display = ("name",)
    
