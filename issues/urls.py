from django.urls import path
from .views import issue_list_view

urlpatterns = [
    path("", issue_list_view, name="issue_list"),
]
