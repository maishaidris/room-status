from django.shortcuts import render, get_object_or_404
# render function generates HTML files using a template & data
from .models import Room, Ticket
from django.views import generic
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import TicketForm


def ticket(request, room_name):
    room_name = get_object_or_404(Room, pk=room_name)

    room = Room.objects.all()

    form_class = TicketForm

    return render(request, 'ticket.html', context={'room_name': room_name, 'room': room, 'form': form_class, })


def index(request):
    '''View function for home page of site'''

    # Generate counts of some of the main objects
    num_rooms = Room.objects.all().count()
    # Generate counts of total number of tickets
    num_tickets = Ticket.objects.all().count()
    # Green rooms (status = 'g')
    num_rooms_green = Room.objects.filter(status__exact='g').all().count()
    # Room Names
    rooms = Room.objects.all()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_rooms': num_rooms, 'num_tickets': num_tickets,
                 'num_rooms_green': num_rooms_green, 'rooms': rooms, },
    )

    # def get_name(request, room_name):
    #     if request.method == 'POST':
    #         form = TicketModelForm(request.POST)
    #         if form.is_valid():
    #             return HttpResponseRedirect('/thanks/')
    #
    #     else:
    #         form = TicketModelForm()
    #
    #     return render(request, 'ticket.html', {'form': form})


def contact(request):
    form_class = ContactForm

    return render(request, 'ticket.html', {'form': form_class, })
