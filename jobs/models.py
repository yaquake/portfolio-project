from django.db import models


class Job(models.Model):
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
