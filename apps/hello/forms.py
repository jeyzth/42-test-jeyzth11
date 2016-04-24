from datetime import date
from django import forms
from django.forms import ModelForm,widgets
from hello.models import Aplicants
import fortytwo_test_task.settings


class FormContact(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormContact,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'}),
        self.fields['surname'].widget.attrs.update({'class': 'form-control'}),
        self.fields['bio'].widget.attrs.update({'class': 'form-control'}),
        self.fields['email'].widget.attrs.update({'class': 'form-control'}),
        self.fields['jabber'].widget.attrs.update({'class': 'form-control'}),
        self.fields['dateofbird'].widget.attrs.update({'class': 'datepicker'}),
        self.fields['skype'].widget.attrs.update({'class': 'form-control'}),
        self.fields['others'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Contacts
        fields = ['name','surname','dateofbird','bio','email','jabber','skype','others']
        widgets = {'dateofbirth': forms.DateInput(attrs={'class': 'datepicker'})
        }


