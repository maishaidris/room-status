from django.shortcuts import render, get_object_or_404, redirect
# render function generates HTML files using a template & data
from .models import Room, Ticket
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import TicketForm
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.template.loader import get_template
from django.contrib import messages


def ticket(request, room_name):
    room_name = get_object_or_404(Room, pk=room_name)

    str_room_name = str(room_name)

    room = Room.objects.all()

    form_class = TicketForm

    if request.method == 'GET':
        form = TicketForm()

    else:
        form = TicketForm(request.POST)

        # validating and cleaning data
        if form.is_valid():
            type_of_issue = form.cleaned_data['type_of_issue']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            feedback_or_further_details = form.cleaned_data['feedback_or_further_details']
            affiliation = form.cleaned_data['affiliation']

            subject = "Issue with " + type_of_issue + " at Room " + str_room_name

            message = "From " + first_name + " " + last_name + \
                " (" + affiliation + ")" + \
                ": " + feedback_or_further_details

            try:
                send_mail(subject, message, email_address, [
                    'son_helpmedia@urmc.rochester.edu', email_address], fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return redirect(request.META['HTTP_REFERER'])

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


# def contact(request):
#     form_class = ContactForm
#
#     return render(request, 'ticket.html', {'form': form_class, })
