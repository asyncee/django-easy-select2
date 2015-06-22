# coding: utf-8

from django import forms
from easy_select2.forms import FixedModelForm
from easy_select2.models import TestFieldsModel


class TestFixedModelForm(FixedModelForm):
    class Meta:
        model = TestFieldsModel
        exclude = []


def test_fixedmodelform():
    form = TestFixedModelForm()
    assert form.fields['fk_field'].help_text.strip() == ''
    assert form.fields['m2m_field'].help_text.strip() == ''
