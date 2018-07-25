from django.forms import ModelForm
from .models import Ticket


class TicketModelForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name']


# class TicketForm(forms.Form):
#     name = forms.CharField(
#         help_text='Please enter your full name.', label='Your name', max_length=100)
