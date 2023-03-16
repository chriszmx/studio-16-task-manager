from django.db import models
from projects.models import Project
from django.conf import settings
# from notes.models import Note

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks"
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    # notes = models.ForeignKey(
    #     Note, on_delete=models.CASCADE,
    #     related_name="notes",
    #     null=True
    # )

    def __str__(self):
        return self.name
