from django.shortcuts import render
# render function generates HTML files using a template & data
from .models import Room, Ticket


def index(request):
    '''View function for home page of site'''

    # Generate counts of some of the main objects
    num_rooms = Room.objects.all().count()
    # Generate counts of total number of tickets
    num_tickets = Ticket.objects.all().count()
    # Green rooms (status = 'g')
    num_rooms_green = Room.objects.filter(status__exact='g').all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_rooms': num_rooms, 'num_tickets': num_tickets,
                 'num_rooms_green': num_rooms_green},
    )
