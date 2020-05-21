# coding: utf-8

from demoapp.models import TestFieldsModel
from easy_select2.forms import FixedModelForm


class TestFixedModelForm(FixedModelForm):
    class Meta:
        model = TestFieldsModel
        exclude = []


def test_fixedmodelform():
    form = TestFixedModelForm()
    assert form.fields['fk_field'].help_text.strip() == ''
    assert form.fields['m2m_field'].help_text.strip() == ''
