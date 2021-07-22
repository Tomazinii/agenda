from django import forms
from django.forms import ModelForm, widgets

from .models import Agenda, Data

class DateInput(forms.DateInput):
    input_type = 'date'
    
class TimeInput(forms.TimeInput):
    input_type = 'time'


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={'class': 'kaquii', 'placeholder' : 'nome do cliente',}),
            "data": DateInput(),
            "hour": TimeInput(),
            "information": forms.Textarea(attrs={'class':'input', 'placeholder':"text......",'rows':8, 'cols':40})     
       }

        labels = {
           'name': "",
           'data' : "",
           "hour" : "",
           "information" : ""

        } 


            
# não é esssssssssssseeeeeeeeeeeeeeeeeeeeee
class DateForm(ModelForm):
    class Meta:
        model = Data
        fields = "__all__"
        widgets = {
            'data': forms.DateInput(),
            'name': forms.TextInput(attrs={'placeholder':'asdf'})
        }
