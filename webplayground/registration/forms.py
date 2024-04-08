from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


# This is a specific user form that will have also the 'email' field
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caractéres como máximo y debe ser válido')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # Function used to detect if an email has already been registered
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # With this we checkall the database filtering by the email to see if it already exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado, prueba con otro.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-2'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografia'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enlace'})
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caractéres como máximo y debe ser válido')

    # With this Meta class we are crossing this form with the model 'user' and its field 'email' for modifications
    class Meta:
        model = User
        fields = ['email']

    # Function used to detect if an email has already been registered
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # First we check if the email has been modified or changed
        if 'email' in self.changed_data:
            # Now we check all the database filtering by the email to see if it already exists
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('El email ya está registrado, prueba con otro.')
        return email
