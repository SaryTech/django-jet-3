from django.contrib import admin

from jet.tests.models import RelatedToTestModel
from jet.tests.models import TestModel


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ("field1", "field2")


@admin.register(RelatedToTestModel)
class RelatedToTestModelAdmin(admin.ModelAdmin):
    pass
