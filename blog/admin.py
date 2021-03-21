from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'message','created_on')
    list_filter = ("subject",)
    search_fields = ['subject', 'message']

    

admin.site.register(Slider)
admin.site.register(Post, PostAdmin)
admin.site.register(contact, ContactAdmin)