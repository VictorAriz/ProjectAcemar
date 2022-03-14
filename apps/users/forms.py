from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import Profile

class userForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'group',
            'password1',
            'password2',
            # 'levels',
        ]
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo Electrónico',
            'group': 'Grupo',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            # 'levels': 'Niveles',
            }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'group': forms.Select(attrs={'class':'form-select'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
            # 'levels': forms.Select(
            #     attrs={
            #         'class': 'form-select',
            #         'placeholder': 'Niveles'
            #         }
            #     ),
        }

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=[
            'phone',
            'levels',
            'singleLevels',
        ]
        labels = {
            'phone': 'Telefono',
            'levels': 'Niveles',
            'singleLevels': 'Nivel individual',
            }
        widgets = {
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'levels': forms.Select(
                attrs={
                    'class': 'form-select',
                    'placeholder': 'Niveles'
                    }
                ),
            'singleLevels': forms.CheckboxSelectMultiple(),
        }

