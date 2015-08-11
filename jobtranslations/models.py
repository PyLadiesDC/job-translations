from django.db import models
from django.utils import timezone

class PasteJobURL(models.Model):
    '''
    A model to paste job URL to the datebase
    along with an "optional" email address. Email
    address used in case user wishes to receive notifications
    '''
    job_URL = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    email = models.EmailField(blank=True)

    def save_pasteJobURL(self):
        self.save()
