from django.shortcuts import render
from django.utils import timezone
from .models import RightIssue

def issue_list_view(request):
    today = timezone.now().date()

    upcoming_issues = RightIssue.objects.filter(
        issue_open_date__gt=today,
        is_published=True,
    ).order_by("issue_close_date")

    open_issues = RightIssue.objects.filter(
        issue_open_date__lte=today,
        issue_close_date__gte=today,
        is_published=True,
    ).order_by("issue_close_date")

    # add days_left
    for issue in upcoming_issues:
        issue.days_left = (issue.issue_open_date - today).days
    for issue in open_issues:
        issue.days_left = (issue.issue_close_date - today).days

    context = {
        "upcoming_issues": upcoming_issues,
        "open_issues": open_issues,
    }

    return render(request, "issues/issue_list.html", context)
