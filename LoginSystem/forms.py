from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from LoginSystem.models import RegistrationData, regulator_master, frequency_master, \
    tax_master, form_return_master


class Registration_form(forms.ModelForm):
    class Meta:
        model = RegistrationData
        fields = ['regulator', 'financial_year', 'assessment_year', 'form_return', 'frequency', 'period_from',
                  'period_to',
                  'type_of_tax_payer', 'actual_due_date', 'Description','latest_due_date']


class Registration_Update(Registration_form):
    due_date_1 = forms.DateField(label="Due Date 1", required=False,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    due_date_1_remarks = forms.CharField(label="Due Date 1 Remarks", required=False,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date_2 = forms.DateField(label="Due Date 2", required=False,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    due_date_2_remarks = forms.CharField(label="Due Date 2 Remarks", required=False,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date_3 = forms.DateField(label="Due Date 3", required=False,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    due_date_3_remarks = forms.CharField(label="Due Date 3 Remarks", required=False,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date_4 = forms.DateField(label="Due Date 4", required=False,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    due_date_4_remarks = forms.CharField(label="Due Date 4 Remarks", required=False,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    due_date_5 = forms.DateField(label="Due Date 5", required=False,
                                 widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    due_date_5_remarks = forms.CharField(label="Due Date 5 Remarks", required=False,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    latest_due_date = forms.CharField(label="Latest Due Date", required=True,
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RegistrationData
        fields = ['due_date_1', 'due_date_1_remarks', 'due_date_2', 'due_date_2_remarks', 'due_date_3',
                  'due_date_3_remarks', 'due_date_4', 'due_date_4_remarks', 'due_date_5', 'due_date_5_remarks','latest_due_date']


class RegularMaster_form(forms.ModelForm):
    class Meta:
        model = regulator_master
        fields = '__all__'


class FrequencyMaster_form(forms.ModelForm):
    class Meta:
        model = frequency_master
        fields = '__all__'


class TaxMaster_form(forms.ModelForm):
    class Meta:
        model = tax_master
        fields = '__all__'


class Form_ReturnMaster_form(forms.ModelForm):
    class Meta:
        model = form_return_master
        fields = '__all__'


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **krwargs):
        super(SignupForm, self).__init__(*args, **krwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['username'].help_text = ' '

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = ' '
