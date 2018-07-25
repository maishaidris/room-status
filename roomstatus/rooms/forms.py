from django import forms
# from django.forms import ModelForm
from .models import Ticket
from .choices import *


class TicketForm(forms.Form):
    type_of_issue = forms.ChoiceField(
        choices=ISSUE_CHOICES, widget=forms.RadioSelect(), required=True)
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'first-name', 'type': 'text', 'name': 'first-name', 'maxlength': '50', 'placeholder': 'First name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'id': 'last-name', 'type': 'text', 'name': 'last-name', 'maxlength': '50', 'placeholder': 'Last name'}))
    email_address = forms.EmailField(required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': 'email', 'id': 'email', 'name': 'email', 'placeholder': 'Email address'}))
    feedback_or_further_details = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'name': 'additional-details', 'placeholder': 'Please enter additional details or your feedback here.'}))
    affiliation = forms.ChoiceField(
        choices=AFFILIATION_CHOICES, widget=forms.CheckboxSelectMultiple(), required=True)
