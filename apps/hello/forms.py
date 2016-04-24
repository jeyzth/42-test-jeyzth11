from datetime import date
from django import forms
from django.forms import ModelForm,widgets
from hello.models import Applicant
import fortytwo_test_task.settings


class ApplicantForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplicantForm,self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'max_length':'20'}),
        self.fields['surname'].widget.attrs.update({'class': 'form-control'}),
        self.fields['bio'].widget.attrs.update({'class': 'form-control'}),
        self.fields['email'].widget.attrs.update({'class': 'form-control'}),
        self.fields['jabber'].widget.attrs.update({'class': 'form-control'}),
        self.fields['dateofbird'].widget.attrs.update({'class': 'datepicker'}),
        self.fields['skype'].widget.attrs.update({'class': 'form-control'}),
        self.fields['others'].widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Applicant
        fields = ['name','surname','dateofbird','bio','email','jabber','skype','others']
        widgets = {'dateofbirth': forms.DateInput(attrs={'class': 'datepicker'})
        }


