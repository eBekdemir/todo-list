from django.db import models
from django.db.models import F
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    class Meta:
        verbose_name = ("Task")
        verbose_name_plural = ("Tasks")
        ordering = [F('complete'), F('dead_line').asc(nulls_last=True)]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    dead_line = models.DateField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("", kwargs={"id": self.id})
