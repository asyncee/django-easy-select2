from django import forms

from easy_select2.utils import apply_select2
from easy_select2 import widgets


def test_apply_select2():
    cls = apply_select2(forms.Select)
    assert cls.__name__ == 'Select2Select'
    assert cls.__bases__ == (widgets.Select2Mixin, forms.Select)
