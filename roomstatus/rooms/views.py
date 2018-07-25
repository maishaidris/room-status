from django.shortcuts import render, get_object_or_404, redirect
# render function generates HTML files using a template & data
from .models import Room, Ticket
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import TicketForm
from django.core.mail import EmailMessage, send_mail, BadHeaderError
from django.template.loader import get_template


def ticket(request, room_name):
    room_name = get_object_or_404(Room, pk=room_name)

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

            try:
                send_mail("Issue/Feedback for Room " + room_name,
                          message, from_email, ['admin@example.com'])

            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return redirect('index')

            # template = get_template('ticket.txt')
            # context = {
            #     'first_name': first_name,
            #     'last_name': last_name,
            #     'email_address': email_address,
            #     'type_of_issue': type_of_issue,
            #     'feedback_or_further_details': feedback_or_further_details,
            #     'affiliation': affiliation,
            # }
            # content = template.render(context)
            #
            # email = EmailMessage(
            #     "New stuff was just sent",
            #     content,
            #     "Your website" + '',
            #     ['maisha_idris@urmc.rochester.edu'],
            #     headers={'Reply-To': contact_email}
            # )

            # send_mail(
            #     'Subject line maihsa',
            #     'Helloooo',
            #     'midris2@u.rochester.edu',
            #     ['maisha627@gmail.com'],
            #     fail_silently=False,
            # )
            # email.send()
            # return redirect('contact')

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
