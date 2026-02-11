from django.contrib import admin
from .models import RightIssue


@admin.register(RightIssue)
class RightIssueAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "issue_open_date",
        "issue_close_date",
        "status_display",
        "is_published",
    )

    list_filter = ("is_published",)
    search_fields = ("company_name",)
    ordering = ("-issue_open_date",)

    def status_display(self, obj):
        return obj.status   # OR obj.is_active if using property

    status_display.short_description = "Status"
