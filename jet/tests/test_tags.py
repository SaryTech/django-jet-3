from django import forms
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from jet.templatetags.jet_tags import jet_next_object
from jet.templatetags.jet_tags import jet_previous_object
from jet.templatetags.jet_tags import jet_select2_lookups
from jet.tests.models import SearchableTestModel
from jet.tests.models import TestModel


class TagsTestCase(TestCase):
    def setUp(self):
        self.models = []
        self.searchable_models = []

        self.user = User.objects.create(username="Test User")
        self.models.append(TestModel.objects.create(field1="first", field2=1))
        self.models.append(TestModel.objects.create(field1="second", field2=2))
        self.searchable_models.append(SearchableTestModel.objects.create(field1="first", field2=1))
        self.searchable_models.append(SearchableTestModel.objects.create(field1="second", field2=2))

    def test_select2_lookups(self):
        class TestForm(forms.Form):
            form_field = forms.ModelChoiceField(SearchableTestModel.objects)

        value = self.searchable_models[0]

        form = TestForm(initial={"form_field": value.pk})
        field = form["form_field"]
        field = jet_select2_lookups(field)
        choices = [choice for choice in field.field.choices]

        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0][0], value.pk)

    def test_select2_lookups_posted(self):
        class TestForm(forms.Form):
            form_field = forms.ModelChoiceField(SearchableTestModel.objects)

        value = self.searchable_models[0]

        form = TestForm(data={"form_field": value.pk})
        field = form["form_field"]
        field = jet_select2_lookups(field)
        choices = [choice for choice in field.field.choices]

        self.assertEqual(len(choices), 1)
        self.assertEqual(choices[0][0], value.pk)

    def test_non_select2_lookups(self):
        class TestForm(forms.Form):
            form_field = forms.ModelChoiceField(TestModel.objects)

        value = self.searchable_models[0]

        form = TestForm(initial={"form_field": value.pk})
        field = form["form_field"]
        field = jet_select2_lookups(field)
        choices = [choice for choice in field.field.choices]

        self.assertEqual(len(choices), len(self.models) + 1)

    def test_jet_sibling_object_next_url(self):
        instance = self.models[0]
        ordering_field = 1  # field1 in list_display
        preserved_filters = "_changelist_filters=o%%3D%d" % ordering_field

        expected_url = (
            reverse(
                f"admin:{TestModel._meta.app_label}_{TestModel._meta.model_name}_change",
                args=(self.models[1].pk,),
            )
            + "?"
            + preserved_filters
        )

        request = RequestFactory().get(expected_url)
        request.user = self.user

        context = {
            "original": instance,
            "preserved_filters": preserved_filters,
            "request": request,
        }

        actual_url = jet_next_object(context)["url"]

        self.assertEqual(actual_url, expected_url)

    def test_jet_sibling_object_previous_url(self):
        instance = self.models[0]
        ordering_field = 1  # field1 in list_display
        preserved_filters = "_changelist_filters=o%%3D%d" % ordering_field

        changelist_url = (
            reverse(
                f"admin:{TestModel._meta.app_label}_{TestModel._meta.model_name}_change",
                args=(self.models[1].pk,),
            )
            + "?"
            + preserved_filters
        )

        request = RequestFactory().get(changelist_url)
        request.user = self.user

        context = {
            "original": instance,
            "preserved_filters": preserved_filters,
            "request": request,
        }

        previous_object = jet_previous_object(context)
        expected_object = None

        self.assertEqual(previous_object, expected_object)
