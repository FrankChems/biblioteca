from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView,View
from django.urls import reverse_lazy
from .forms import AutorForm,LibroForm
from .models import Autor,Libro



class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/listar_autor.html'

    #retorna la consulta que se realizara en toda la clase
    def get_queryset(self):
        return self.model.objects.filter(estado=True).order_by('-id')
    
    #retorna los datos de la consulta
    def get_context_data(self,**kwargs):
        contexto = {}
        contexto['autores'] = self.get_queryset()
        contexto['form'] = self.form_class()
        return contexto
    
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name,self.get_context_data())

"""
class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset =  Autor.objects.filter(estado=True).order_by('-id')

"""

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('listar_autor')

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('listar_autor')


class EliminarAutor(DeleteView):
    model = Autor
    

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id = pk)

        object.estado = False
        object.save()

        return redirect('listar_autor')


class ListadoLibros(View):
    #Funcion dentro de una vista basada en clase. Con todo esto podremos crear libros
    model = Libro
    form_class= LibroForm
    template_name = 'libro/libro/listar_libro.html'
    
    def get_queryset(self):
        return self.model.objects.filter(estado = True).order_by('-id')

    def get_context_data(self, **kwargs):
        context = {}
        context["libros"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,self.get_context_data())
    
   

#esta view se utiliza como modal de crear libro
class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro/crear_libro.html"
    success_url = reverse_lazy('listado_libros')


class ActualizarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro/libro.html"
    success_url = reverse_lazy('listado_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['libros'] = Libro.objects.filter(estado = True)
        return context

class EliminarLibro(DeleteView):
    model = Libro 


    def post(self,request,pk,*args,**kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('listado_libros')