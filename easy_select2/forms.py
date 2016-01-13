# coding: utf-8

from django import forms
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

M = _('Hold down "Control", or "Command" on a Mac, to select more than one.')


class FixedModelForm(forms.ModelForm):
    """
    Simple child of ModelForm that removes the 'Hold down "Control" ...'
    message that is enforced in select multiple fields.

    See https://github.com/asyncee/django-easy-select2/issues/2
    and https://code.djangoproject.com/ticket/9321
    """

    def __init__(self, *args, **kwargs):
        super(FixedModelForm, self).__init__(*args, **kwargs)

        msg = force_text(M)

        for name, field in self.fields.items():
            field.help_text = field.help_text.replace(msg, '')
