from django.db import models
from django.urls import reverse
import uuid  # For unique ticket IDs
from .choices import *


class Room(models.Model):
    '''Model representing a room found in HWH (but not a specific room)'''

    name = models.CharField(max_length=100, primary_key=True, unique=True)
    image = models.ImageField()
    # how to add history: tuple field?
    # how to add pending_tickets: {dict} field?
    details = models.TextField(null=True, blank=True)
    floorplan = models.ImageField(null=True, blank=True)

    ROOM_STATUS = (
        ('r', 'Red'),
        ('y', 'Yellow'),
        ('g', 'Green'),
    )

    status = models.CharField(max_length=1, choices=ROOM_STATUS,
                              blank=True, default='g', help_text='Status of the room')

    no_new_tickets = models.BooleanField(default=True)

    def __str__(self):
        '''String for representing the Room object'''
        return self.name

    def get_absolute_url(self):
        '''Returns the url to access a detail record for this book'''
        return reverse('room-detail', arg=[str(self.id)])

    class Meta:
        ordering = ['name']


class Ticket(models.Model):
    '''Model representing a user's ticket'''

    ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                     help_text='Unique ID for this particular ticket across all the available tickets')
    room_name = models.ForeignKey(
        Room, null=True, on_delete=models.PROTECT)
    #issue_type: radio
    # issue_specificity: checklist, JS?
    additional_information_feedback = models.TextField(null=True, blank=True)

    affiliation = models.CharField(max_length=15, choices=AFFILIATION_CHOICES,
                                   default=FACULTY, help_text='Affiliation with the SON', null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        '''String for represerting the Model object'''

        return '{0} ({1})'.format(self.ticket_number, self.additional_information_feedback)
