from django.db import models
import datetime



# Create your models here.
class Campaign(models.Model):
    """
    A campaign that a user can subscribe to.

    Currently, we don't have ManyToMany support so
    a user is assumed to be part of only one campaign.
    """
    name = models.CharField(max_length=30, unique=True)
    start_date = models.DateTimeField(default=datetime.datetime.now)
    geographic_area = models.CharField(max_length=30)
    # participants will be many to many field   
    # stores

class Store(models.Model):
    """
    A store that is part of a campaign
    """
    name = models.CharField(max_length=30, unique=True)
    campaign = models.ForeignKey(Campaign)
