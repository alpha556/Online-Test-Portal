from django.contrib import admin
from .models import Exam, Question, Report


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Question
    extra = 1


class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['exam_name']}),
        ('Date Information', {'fields': ['date_published', 'duration']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('exam_name','duration', 'date_published')

admin.site.register(Exam, ExamAdmin)
admin.site.register(Report)