from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class Contact(models.Model):
    message = models.CharField(max_length = 250, null = True, blank = False)
    subject = models.CharField(max_length = 20, null = True, blank = False)
    email = models.EmailField(null = False, blank = False)
    
    def __unicode__(self):
        return smart_unicode(self.email)