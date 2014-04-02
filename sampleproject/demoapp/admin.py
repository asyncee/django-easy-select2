from django.contrib import admin
from django import forms

from easy_select2 import select2_modelform_meta, Select2TextInput

from .models import Tag, Note, MarkupType


class NoteAdminForm(forms.ModelForm):
    Meta = select2_modelform_meta(Note)

    def __init__(self, *args, **kwargs):
        super(NoteAdminForm, self).__init__(*args, **kwargs)
        markup_data = list(MarkupType.objects.all().values('id', 'text'))
        # dynamically override widget with existing markup choices
        self.fields['markup'].widget = Select2TextInput(select2attrs={'data': markup_data})

    def clean(self):
        # process dirty data and fill cleaned_data with correct markup id
        dirty_markup = self.data['markup']
        try:
            markup = MarkupType.objects.get(id=int(dirty_markup))
        except (ValueError, MarkupType.DoesNotExist):
            markup = MarkupType.objects.create(text=dirty_markup)

        cleaned_data = super(NoteAdminForm, self).clean()
        self.cleaned_data['markup'] = markup.id
        return cleaned_data


class NoteAdmin(admin.ModelAdmin):
    form = NoteAdminForm


admin.site.register(Tag)
admin.site.register(MarkupType)
admin.site.register(Note, NoteAdmin)
