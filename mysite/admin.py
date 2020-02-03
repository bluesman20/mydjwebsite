from django.contrib import admin

# Register your models here.

from mysite.models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'alias', 'is_public']
    search_fields = ['title']
    list_filter = ['is_public']
    list_editable = ['is_public']
    
admin.site.register(Page, PageAdmin)
