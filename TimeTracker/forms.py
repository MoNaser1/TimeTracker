from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.timezone import localtime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from .models import Company, Employee, Post



class dateTime(forms.DateInput):
    input_type = 'datetime-local'


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))
    start_time = forms.DateTimeField(widget=dateTime(), input_formats='%d/%m/%y %H:%M:%S')
    end_time = forms.DateTimeField(widget=dateTime(), input_formats='%d/%m/%y %H:%M:%S')
    # employee = forms.CharField()

    class Meta:
        model = Post
        fields = '__all__'





class MyCustomSignupForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'E-mail'}),  label='')
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Full Name'}), label='')
    company = forms.ModelChoiceField(queryset=Company.objects.all(), to_field_name='name')
    password1 = forms.CharField(
        label=(''),

        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=(""),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': 'Password (Again)'}),
        strip=False,
        # help_text= ("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "company"]
        # field_classes = {'compony': Company.name,
        #                  'username': Employee.name,
        #                  }

