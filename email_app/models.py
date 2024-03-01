# email_app/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class EmailInfo(models.Model):
    to_email = models.EmailField()
    company_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=255)  # Add the purpose field
    message_content = RichTextUploadingField()

    def __str__(self):
        return self.to_email
