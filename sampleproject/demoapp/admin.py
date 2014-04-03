from django.contrib import admin
from django import forms

from easy_select2 import select2_modelform_meta, Select2TextInput

from .models import Note, Category


class NoteAdminForm(forms.ModelForm):
    Meta = select2_modelform_meta(Note)

    def __init__(self, *args, **kwargs):
        super(NoteAdminForm, self).__init__(*args, **kwargs)

        #
        # Let's create the *current* list of choices for the mood field. By
        # putting this code here, it will ensure that the list is up-to-date
        # for each usage of the form.
        #
        # Also, you could personalize the experience by filtering the query to
        # only those Notes previously edited by this user. The effect would be
        # that each project Admin would see only their personal list of moods
        # that they've used in the past.
        #
        # You should note, that we are using denormalized table
        # structure there, what perfectly solves the problem.
        #
        mood_data = Note.objects.values_list('mood', flat=True).order_by('mood')

        self.fields['mood'].widget = Select2TextInput(select2attrs={
            #
            # This is how Select2 expects the list of choices.
            #
            'data': [{'id': x, 'text': x} for x in mood_data]
        })


class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm


admin.site.register(Category)
admin.site.register(Note, NoteAdmin)
