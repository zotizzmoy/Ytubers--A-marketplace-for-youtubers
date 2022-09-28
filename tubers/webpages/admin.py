from django.contrib import admin
from .models import Slider, Team

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)