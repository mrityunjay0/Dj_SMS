from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'age',
        'english_marks',
        'maths_marks',
        'display_total',
        'display_result',
    )


    search_fields = ('name',)

    list_filter = ('age',)

    ordering = ('id',)


    @admin.display(description='Total Marks')
    def display_total(self, obj):
        return obj.total_marks


    @admin.display(description='Result')
    def display_result(self, obj):
        return obj.result
