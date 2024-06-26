from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset
from crispy_forms.bootstrap import StrictButton, InlineField
from .models import *
from .choices import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = ['name', 'gender', 'age', 'current_status', 'identity', 'unemployment_duration']

    field_order = ['name', 'gender', 'age', 'current_status', 'identity', 'unemployment_duration']

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                }),
        label='姓名')
    
    gender = forms.ChoiceField(choices=choices_gender, widget=forms.RadioSelect(), label='性別', )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                }),
        label='年齡')
        
    # education = forms.ChoiceField(
    #     required=False,
    #     choices=choices_education,
    #     widget=forms.Select(
    #         attrs={
    #             }),
    #     label='學歷')
    
    current_status = forms.MultipleChoiceField(
        choices=choices_current,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                }),
        label='就業狀況')
    
    identity = forms.MultipleChoiceField(
        choices=choices_identity,
        widget=forms.CheckboxSelectMultiple(
            attrs={
                }),
        label='身份別')
    
    unemployment_duration = forms.ChoiceField(
        required=False,
        choices=choices_unemployment_duration,
        widget=forms.RadioSelect(
            attrs={
                'class': 'employee-form',
                }),
        label='失業週期')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            # Set all fields css_class to form-label
            # Field('name', css_class='form-label'),
            # Field('gender', css_class='form-label'),
            # Field('age', css_class='form-label'),
            # Field('unemployment_duration', css_class='form-label'),
            # Field('current_status', css_class='form-label'),
            # Field('identity', css_class='form-label'),
        )
    
    