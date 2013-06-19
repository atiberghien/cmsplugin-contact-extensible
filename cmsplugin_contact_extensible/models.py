from django.db import models
from cmsplugin_contact.models import BaseContact

class CustomContact(BaseContact):
    allow_attachment = models.BooleanField(default=False)
    extra_fields = models.TextField()
    