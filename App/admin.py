from django.contrib import admin
from App.models import Student
from django.http import HttpResponse
from django.core import serializers


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    actions = ["export_as_json"]

    def export_as_json(modeladmin, request, queryset):
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response


# Register your models here.
admin.site.register(Student, StudentAdmin)

