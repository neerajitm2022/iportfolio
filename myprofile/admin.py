from django.contrib import admin
from . models import About



class AboutAdmin(admin.ModelAdmin):
   list_display = ('description', 'birthday', 'website', 'phone')
   class Meta:
        ordering = "name"
    
admin.site.register(About, AboutAdmin)
# Register your models here.
