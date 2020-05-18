from django.contrib import admin

from easy_select2 import select2_modelform

from .models import Note, Category


class NoteAdmin(admin.ModelAdmin):
    form = select2_modelform(Note)


admin.site.register(Category)
admin.site.register(Note, NoteAdmin)
