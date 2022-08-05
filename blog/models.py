import imp
from statistics import mode
from venv import create
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  create_date = models.DateField(default=timezone.now)
  published_date = models.DateField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()

  def __str__(self) -> str:
    return self.title