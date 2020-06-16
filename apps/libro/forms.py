from django import forms
from .models import Autor,Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre','apellidos','nacionalidad','descripcion'
        ]
        labels = {
            'nombre': 'Nombre del autor',
            'apellidos' : 'Apellidos del autor',
            'nacionalidad' : 'Nacionalidad del autor',
            'descripcion' : 'Pequeña descripción',
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder' : 'Ingrese nombre del autor',
                    'id' : 'nombre',
                }
            ),
            'apellidos' :forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese apellidos del autor',
                    'id': 'apellidos'
                }
            ),
            'nacionalidad' :forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la nacionalidad del autor',
                    'id': 'nacionalidad'
                }
            ),
            'descripcion' :forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese descripción del autor',
                    'id': 'descripcion'
                }
            ),
        } 

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('titulo','autor_id','fecha_publicacion')
        label = {
            'titulo':'Titulo del Libro',
            'autor_id':'Autor del libro',
            'fecha_publicacion':'Fecha de publicación'

        }
        widgets = {
            'titulo':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese libro'
                }
            ),
            'autor_id':forms.Select(
                 attrs = {
                    'class':'form-control'
                 }
            ),
            'fecha_publicacion':forms.SelectDateWidget(
                attrs ={
                    'class':'form-control'
                }
            )
        }
