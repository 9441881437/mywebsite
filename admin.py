from django.contrib import admin
from playground.models import *

# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display = ('username', 'surname', 'email')

admin.site.register(FormModels, FormAdmin)
    