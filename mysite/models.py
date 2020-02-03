from django.db import models
from tinymce import models as tinymce_models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=250)
    alias = models.CharField(max_length=250)
    content = tinymce_models.HTMLField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title 