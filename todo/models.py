from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40, db_index=True)

    def __str__(self):
        return f"{self.title}"
