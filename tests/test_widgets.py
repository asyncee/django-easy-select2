from collections import OrderedDict

import mock
import pytest
from django.contrib.staticfiles.storage import staticfiles_storage

from easy_select2 import widgets


def test_select2mixin_constructor():
    s = widgets.Select2Mixin()
    assert isinstance(s.select2attrs, dict)
    assert s.select2attrs['width'] == '250px'

    s1 = widgets.Select2Mixin(select2attrs={'auto': True})
    assert s1.select2attrs['auto'] == True

    with pytest.raises(AssertionError):
        widgets.Select2Mixin(select2attrs="wrong value")


def test_select2mixin_get_options():
    s = widgets.Select2Mixin()
    assert isinstance(s.get_options(), dict)


def test_select2mixin_render_options_code():
    s = widgets.Select2Mixin()
    options = OrderedDict()
    options['number'] = 1
    options['string'] = u'string'
    options['dict'] = {'k': 'v'}
    options['list'] = [1, 'two']
    result = s.render_select2_options_code(options, 'some_id')
    expected = (
        "data-number='1' "
        "data-string='string' "
        "data-dict='{\"k\": \"v\"}' "
        "data-list='[1, \"two\"]'"
    )
    assert result == expected


@mock.patch.object(widgets.Select2Mixin, 'render_select2_options_code')
def test_select2mixin_render_js_code(mocked):
    mocked.return_value = "some_options"
    s = widgets.Select2Mixin()
    s.html = "{id}: {options}"
    result = s.render_js_code("some_id")
    expected = "some_id: some_options"
    assert result == expected


def test_select2mixin_render_js_code_should_return_empty_string():
    s = widgets.Select2Mixin()
    assert s.render_js_code(id_=None) == u''


class SuperWithRender(object):
    def render(self, *args, **kwargs):
        return "super"


class TestRender(widgets.Select2Mixin, SuperWithRender):
    pass


@mock.patch.object(TestRender, 'render_js_code')
def test_select2mixin_render(mocked):
    mocked.return_value = "some_js"
    s = TestRender()
    result = s.render('name', 'value', attrs={'id': 'some_id'})
    expected = "supersome_js"
    assert result == expected


def test_staticfiles_url(settings):
    js = widgets.SELECT2_WIDGET_JS
    css = widgets.SELECT2_WIDGET_CSS

    def all_startswith(string, iterable):
        return all([staticfiles_storage.url(x).startswith(string)
                    for x in iterable])

    assert all_startswith(
            settings.STATIC_URL,
            js,
    )
    for v in css.values():
        assert all_startswith(
                settings.STATIC_URL,
                v,
        )
