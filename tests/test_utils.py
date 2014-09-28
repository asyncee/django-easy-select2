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


def test_select2_meta_factory_noargs_empty_model():
    cm = utils.select2_meta_factory(m.EmptyModel)
    assert cm.__name__ == 'Meta'
    assert cm.__bases__ == (object,)
    assert cm.model == m.EmptyModel
    assert cm.widgets == {}


def test_select2_meta_factory_attributes_noargs():
    cm = utils.select2_meta_factory(m.TestFieldsModel)
    assert cm.__name__ == 'Meta'
    assert cm.__bases__ == (object,)
    assert cm.model == m.TestFieldsModel
    assert cm.widgets != {}
    assert cm.widgets['fk_field'].__class__.__name__ == 'Select2'
    assert cm.widgets['choice_field'].__class__.__name__ == 'Select2'
    assert cm.widgets['m2m_field'].__class__.__name__ == 'Select2Multiple'


# Select2 has already been imported by easy_select2.utils module
@mock.patch('easy_select2.utils.Select2Multiple')
@mock.patch('easy_select2.utils.Select2')
def test_select2_meta_factory_calls_noargs(Select2Mock, Select2MultipleMock):
    utils.select2_meta_factory(m.TestFieldsModel)
    Select2Mock.assert_called_with(select2attrs=None)
    assert Select2Mock.call_count == 2
    Select2MultipleMock.assert_called_with(select2attrs=None)
    assert Select2MultipleMock.call_count == 1


# TODO: test calls with different arguments
