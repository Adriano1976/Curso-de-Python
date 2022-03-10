"""
- Se você tiver di¦culdade em encontrar onde os arquivos do Django estão localizados em seu sistema,
execute o seguinte comando:  python -c "import django; print(django.__path__)"
- Caminho: venv/Lib/site-packages/django/contrib/admin/sites.py
"""

from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Informações', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
