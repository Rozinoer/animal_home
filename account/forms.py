from django import forms
from django.contrib.auth.models import User
from .models import Profile, Shelter
from shelter.models import Animal


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class AnimalRegistrationForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_card', 'animal_name', 'animal_kind', 'animal_gender', 'animal_color',
                  'animal_ears', 'animal_tail', 'animal_age', 'animal_breed', 'animal_size',
                  'animal_wool', 'area', 'photo')
        widgets = {
            'user_id': forms.HiddenInput(),
        }


class ShelterRegistrationForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ('address', 'email', 'phone')
        widgets = {
            'user': forms.HiddenInput(),
        }


class ShelterEditForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ('address', 'email', 'phone')
        widgets = {
            'user': forms.HiddenInput(),
        }


class AnimalEditForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('animal_card', 'animal_name', 'animal_kind', 'animal_gender', 'animal_color',
                  'animal_ears', 'animal_tail', 'animal_age', 'animal_breed', 'animal_size',
                  'animal_wool', 'area', 'photo')
