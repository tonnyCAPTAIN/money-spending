from django import forms
from account.models import Civil_servant
from django.core import validators




# class Civil_servantForm(forms.Form):
#     class Meta:
#         model = Civil_servant
#         fields = '__all__'







class RegisterForm(forms.Form):
    first_name = forms.CharField(label='first name', max_length=100)
    last_name = forms.CharField(label='last name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(widget= forms.PasswordInput, validators=[validators.MinLengthValidator(6)])
    re_password = forms.CharField(widget= forms.PasswordInput, required = False)
    

    # def clean(self):
    #     cleaned_data = super(RegisterForm, self).clean()
    #     first_name = cleaned_data.get('first_name')
    #     last_name = cleaned_data.get('last_name')
    #     username = cleaned_data.get('username')
    #     email = cleaned_data.get('email')
    #     password = cleaned_data.get('password')
    #     re_password = cleaned_data.get('re_password')

    #     if not first_name and not last_name and not username and not email and not password and not re_password:
    #         raise forms.ValidationError('You have to write something !!')



class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput) #min_length=5),




class SalaryForm(forms.Form):
    salary = forms.IntegerField(label='ENTER SALARY')