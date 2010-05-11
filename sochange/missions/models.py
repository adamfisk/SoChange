from django.db import models
import datetime

## different levels of participation
#PARTICIPATION_CHOICES = (
#        ('Gold', 'Gold Level Participation'),
#        ('Silver', 'Silver Level Participation'),
#        ('Bronze', 'Bronze Level Participation'),
#)
#
## Create your models here.
class Mission(models.Model):
#    """
#    A campaign that a user can subscribe to.
#
#    Currently, we don't have ManyToMany support so
#    a user is assumed to be part of only one campaign.
#    """
    name = models.CharField(max_length=50, unique=True)
    short_description = models.TextField()
    long_description = models.TextField()
#    # logo = image
#    shortDescription = models.TextField()
#    longDescription = models.TextField() 
#    startDate = models.DateField()
#    endDate = models.DateField()
#    categories_of_participation = models.CharField(max_length=30, choices=PARTICIPATION_CHOICES)
#    # users 
#    # individual user campaign impact
#    #campaign_impact > graphs
#
#    info = models.TextField
#    start_date = models.DateTimeField(default=datetime.datetime.now)
#    geographic_area = models.CharField(max_length=30)
#    # participants will be many to many field   
#    # stores
#
#class Business(models.Model):
#    """
#    A store that is part of a campaign
#    """
#    name = models.CharField(max_length=30, unique=True)
#    campaig
