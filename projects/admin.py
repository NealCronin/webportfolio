from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={
                'rows': 40,
                'cols': 120,
            })
        },
    }