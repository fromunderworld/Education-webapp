from django.contrib import admin
from .models import RequestLog, Post, Comment 

# Register your models here.

@admin.register(RequestLog)
class RequestLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'ip_address', 'path', 'method')
    list_filter = ('method',)
    search_fields = ('ip_address', 'path')
    
admin.site.register(Post)
admin.site.register(Comment)