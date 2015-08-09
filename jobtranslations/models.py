from django.db import models
from django.utils import timezone

class Paste(models.Model):
    job_description = models.TextField()
    job_qualifications = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    paster_email = models.EmailField()

    def saved_paste(self):
        self.save()



class NLP(models.Model):
    paste = models.ForeignKey('Paste')
    pass



class JobPost(models.Model):
    pass
    '''
    *Company name*
    *Company address*
    *Company phone number* (I dont think we need this. If you have different view, please share it)
    *Salary*
    *Term
    point of contact encrypted email
    '''
