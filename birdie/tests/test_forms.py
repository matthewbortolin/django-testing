#test_forms.py
import pytest
pytestmark = pytest.mark.django_db

from .. import forms

class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert form.is_valid() is False, 'Should be invalid if no data given'

        form = forms.PostForm(data={'body': 'Hello'})
        assert form.is_valid() is False, 'Should be invalid if too short'
        assert 'body' in form.errors, 'Should have body field errors'

        form = forms.PostForm(data={'body': 'Hello World!!!!'})
        assert form.is_valid() is True, 'Should be valid form if long enough'



