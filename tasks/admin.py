from django.contrib import admin

from .models import Tag, Tarefa


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("content", "completed", "created_at", "deadline")
    list_filter = ("completed", "tags")
    search_fields = ("content",)
    filter_horizontal = ("tags",)


admin.site.register(Tag)
