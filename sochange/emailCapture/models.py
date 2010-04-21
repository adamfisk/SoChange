from django.db import models
from django.forms import ModelForm

# Create your models here.
class EmailAddress(models.Model):
    email = models.EmailField()

    def __unicode__(self):
        return self.email

class EmailAddressForm(ModelForm):
    class Meta:
        model = EmailAddress 
