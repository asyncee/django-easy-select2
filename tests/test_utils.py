from __future__ import print_function

import mock

from django import forms

from easy_select2 import utils
from easy_select2 import widgets
from easy_select2 import models as m


def test_apply_select2():
    cls = utils.apply_select2(forms.Select)
    assert cls.__name__ == 'Select2Select'
    assert cls.__bases__ == (widgets.Select2Mixin, forms.Select)


def test_select2_meta_factory_empty_widgets():
    cm = utils.select2_meta_factory(m.EmptyModel)
    assert cm.__name__ == 'Meta'
    assert cm.__bases__ == (object,)
    assert cm.model == m.EmptyModel
    assert cm.widgets == {}


def test_select2_meta_factory_widgets_without_arguments():
    cm = utils.select2_meta_factory(m.TestFieldsModel)
    assert cm.__name__ == 'Meta'
    assert cm.__bases__ == (object,)
    assert cm.model == m.TestFieldsModel
    assert cm.widgets != {}
    assert isinstance(cm.widgets['fk_field'], widgets.Select2)
    assert isinstance(cm.widgets['choice_field'], widgets.Select2)
    assert isinstance(cm.widgets['m2m_field'], widgets.Select2Multiple)
    assert 'text' not in cm.widgets


def test_select2_meta_factory_with_arguments():
    cm = utils.select2_meta_factory(
        m.TestFieldsModel,
        meta_fields={'extra_field': 1},
        widgets={
            'text': forms.TextInput,
            'fk_field': forms.TextInput,  # must change to Select2
        },
    )
    assert cm.extra_field == 1
    assert cm.widgets['text'] == forms.TextInput
    assert isinstance(cm.widgets['fk_field'], widgets.Select2)


# Select2 has already been imported by easy_select2.utils module
@mock.patch('easy_select2.utils.Select2Multiple')
@mock.patch('easy_select2.utils.Select2')
def test_select2_meta_factory_with_blank_attrs_argument(
        Select2Mock, Select2MultipleMock):
    utils.select2_meta_factory(m.TestFieldsModel)
    Select2Mock.assert_called_with(select2attrs=None)
    assert Select2Mock.call_count == 2
    Select2MultipleMock.assert_called_with(select2attrs=None)
    assert Select2MultipleMock.call_count == 1


# Select2 has already been imported by easy_select2.utils module
@mock.patch('easy_select2.utils.Select2Multiple')
@mock.patch('easy_select2.utils.Select2')
def test_select2_meta_factory_with_attrs_argument(
        Select2Mock, Select2MultipleMock):
    attrs = {'attribute': True}
    utils.select2_meta_factory(m.TestFieldsModel, attrs=attrs)
    Select2Mock.assert_called_with(select2attrs=attrs)
    assert Select2Mock.call_count == 2
    Select2MultipleMock.assert_called_with(select2attrs=attrs)
    assert Select2MultipleMock.call_count == 1


def test_select2_modelform():
    form_class = utils.select2_modelform(m.TestFieldsModel)
    assert form_class.__name__ == 'TestFieldsModelForm'
    assert form_class.__bases__ == (forms.ModelForm,)
    assert hasattr(form_class, 'Meta') == True


def test_select2_modelform_form_class_argument():
    class TestForm(forms.ModelForm):
        pass
    form_class = utils.select2_modelform(
        m.TestFieldsModel,
        form_class=TestForm,
    )
    assert form_class.__name__ == 'TestFieldsModelForm'
    assert form_class.__bases__ == (TestForm,)
    assert hasattr(form_class, 'Meta') == True


@mock.patch('easy_select2.utils.select2_modelform_meta')
def test_select2_modelform_attrs_argument(mock):
    utils.select2_modelform(m.TestFieldsModel)
    mock.assert_called_with(m.TestFieldsModel, attrs=None)
    attrs = {'attr': False}
    utils.select2_modelform(m.TestFieldsModel, attrs=attrs)
    mock.assert_called_with(m.TestFieldsModel, attrs=attrs)

