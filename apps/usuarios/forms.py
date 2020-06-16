from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class FormularioLogin(AuthenticationForm):

    def __init__(self,*args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class FormularioUsuario(forms.ModelForm):
    """Formulario de registro de un usuario en la base de datos
    """
    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese contraseña',
            'id':'password1',
            'required':'required',

        }
    ))

    password2 = forms.CharField(label = 'Confirmar contraseña', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente contraseña',
            'id':'password2',
            'required':'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombres','apellidos')
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo electronico'
                }
            ),
            'nombres':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre'
                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese sus apellidos'
                }
            ),
            'username':forms.TextInput(
                attrs={
                      'class':'form-control',
                    'placeholder':'Ingrese nombre de usuario'
                }
            )
        }

    def clean_password2(self):
        #validacion de  contraseña
        #metodo que valida ambas contraseñas ingresadas sean iguales, eso antes de ser encriptadas

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user