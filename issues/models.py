import uuid
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel

class UUIDMixin(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)

    class Meta:
        abstract = True

class RightIssue(UUIDMixin):

    company_name = models.CharField(max_length=255)

    issue_open_date = models.DateField()
    issue_close_date = models.DateField()

    apply_link = models.URLField(blank=True, null=True)

    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-issue_open_date"]

    def __str__(self):
        return self.company_name

    @property
    def status(self):
        today = timezone.now().date()

        if today < self.issue_open_date:
            return "upcoming"
        elif self.issue_open_date <= today <= self.issue_close_date:
            return "open"
        return "closed"
