import datetime
from datetime import time

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from app1.models import customuser, batch, equipments, complaints, servicemodel, \
    creditcard, Bill, schedule, attendancemodel, firstaid, appointment
from tempus_dominus.widgets import TimePicker


class customuserform(UserCreationForm):
    class Meta:
        model = customuser
        fields = ('first_name','last_name',
                  'username','password1','password2',
                  'phone_number','email','address')


gender_choice = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

class instructorform(UserCreationForm):
    gender = forms.ChoiceField(choices=gender_choice,required=True,widget=forms.RadioSelect)
    class Meta:
        model = customuser
        fields = ('first_name','last_name','username',
                  'password1','password2','phone_number',
                  'address','experience',
                  'photo','date_of_birth','gender')
        widgets = {
            'date_of_birth':forms.widgets.DateInput(attrs={'type':'date'})
        }

class physicianform(UserCreationForm):
    class Meta:
        model = customuser
        fields = ('first_name','last_name','username','password1',
                  'password2','phone_number','address','qualification')


class batchform(forms.ModelForm):
    class Meta:
        model = batch
        fields = ('batch_time','batch_name')
        widgets = {
            'batch_time':forms.widgets.TimeInput(attrs={'type':'time'})
        }

class machineform(forms.ModelForm):
    class Meta:
        model = equipments
        fields = ('machine_name','machine_photo')

class complaintsform(forms.ModelForm):
    class Meta:
        model = complaints
        fields = ('subject','description','date')
        widgets={
            'date':forms.widgets.DateInput(attrs={'type':'date'})
        }

class replyform(forms.ModelForm):
    class Meta:
        model = complaints
        fields = ('reply',)


class serviceform(forms.ModelForm):
    class Meta:
        model = servicemodel
        fields = ('services','image')

class firstaidform(forms.ModelForm):
    class Meta:
        model = firstaid
        fields = ('name','image')

attendance_choice = (
    ('PRESENT','PRESENT'),
    ('ABSENT','ABSENT')
)

class attendanceform(forms.ModelForm):
    attendance = forms.ChoiceField(choices=attendance_choice,widget=forms.RadioSelect)
    class Meta:
        model = attendancemodel
        fields = ('customer','attendance','date')
        widgets = {
            'date':forms.widgets.DateInput(attrs={'type':'date'})
        }

class billform(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ('name','bill_date','amount')


class paybillform(forms.ModelForm):
    card_no = forms.CharField(validators=[RegexValidator(regex='^.{16}$', message='Please Enter a Valid Card No')])
    card_cvv = forms.CharField(widget=forms.PasswordInput,validators=[RegexValidator(regex='^.{3}$', message='Please Enter a vaid CVV')])
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = creditcard
        fields = ('card_no','card_cvv','expiry_date')

        def clean(self):
            cleaned_data = super().clean()
            expiry_date = cleaned_data.get("expiry_date")

            if (expiry_date < datetime.date.today()):
                raise forms.ValidationError("This card has Expired")

            return cleaned_data

class scheduleform(forms.ModelForm):
    class Meta:
        model = schedule
        fields = ('physician_name','start_time','end_time','date',)
        widgets = {
            'start_time': forms.widgets.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.widgets.TimeInput(attrs={'type': 'time'}),
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }

class appointmentform(forms.ModelForm):
    class Meta:
        model = appointment
        fields = ('physician_name','Schedule_appointment')






