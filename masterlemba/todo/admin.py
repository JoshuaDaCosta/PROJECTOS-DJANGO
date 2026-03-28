from datetime import date

from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "usuario",
        "data_entrega",
        "criado_em",
        "finalizado_em",
        "status",
    )
    list_filter = ("usuario", "data_entrega", "criado_em", "finalizado_em")
    search_fields = ("titulo", "usuario__username", "usuario__email")
    ordering = ("data_entrega", "-criado_em")
    date_hierarchy = "data_entrega"
    list_select_related = ("usuario",)
    readonly_fields = ("criado_em", "finalizado_em")
    actions = ("marcar_completo",)

    @admin.display(description="Status", boolean=True)
    def status(self, obj):
        return bool(obj.finalizado_em)

    @admin.action(description="Marcar como completo (hoje)")
    def marcar_completo(self, request, queryset):
        queryset.filter(finalizado_em__isnull=True).update(finalizado_em=date.today())
