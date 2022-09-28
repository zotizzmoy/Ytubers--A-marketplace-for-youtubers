from django.contrib import admin
from .models import Youtuber

# Register your models here.
class YtAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'subs_count', 'is_featured')
    search_fields = ('firstname', 'lastname', 'camera')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'firstname', 'lastname')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, YtAdmin)
