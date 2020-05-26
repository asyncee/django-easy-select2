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
    assert s1.select2attrs['auto'] is True

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
    s = widgets.Select2Mixin()
    js = s.media._js
    css = s.media._css

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


def test_django_jquery__bundled(settings):
    settings.SELECT2_USE_BUNDLED_JQUERY = True
    s = widgets.Select2Mixin()
    assert s.media._js[0].startswith('easy_select2/vendor/jquery/jquery-')
    assert s.media._js[0].endswith('.min.js')


def test_django_jquery__not_bundled(settings):
    settings.SELECT2_USE_BUNDLED_JQUERY = False
    s = widgets.Select2Mixin()
    assert s.media._js[0] == 'admin/js/jquery.init.js'


def test_django_select2__bundled(settings):
    settings.SELECT2_USE_BUNDLED_SELECT2 = True
    s = widgets.Select2Mixin()
    assert s.media._css['screen'][0].startswith('easy_select2/vendor/select2-')
    assert s.media._css['screen'][0].endswith('/css/select2.min.css')
    assert s.media._js[3].startswith('easy_select2/vendor/select2-')
    assert s.media._js[3].endswith('/js/select2.min.js')


def test_django_select2__not_bundled(settings):
    settings.SELECT2_USE_BUNDLED_SELECT2 = False
    s = widgets.Select2Mixin()
    assert s.media._css['screen'][0] == 'admin/css/vendor/select2/select2.min.css'
    assert s.media._js[3] == 'admin/js/vendor/select2/select2.full.min.js'
