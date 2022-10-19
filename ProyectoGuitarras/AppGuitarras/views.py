from django.shortcuts import render
from django.http import HttpResponse
from AppGuitarras.forms import *
from AppGuitarras.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin   
from django.contrib.auth.decorators import login_required


# Create your views here.

def inicio(request):
    return render(request, "AppGuitarras/inicio.html")



def fender(request):

    fender1 = Fender(fenderguitarra="Stratocaster", serie="154286")
    fender1.save()

    return render(request, "AppGuitarras/fender.html")

def gibson(request):

    gibson1 = Gibson(gibsonguitarra="LesPaul", serie="735469")
    gibson1.save()

    return render(request, "AppGuitarras/gibson.html")

def ibanez(request): 

    ibanez1 = Ibanez(ibanezguitarra="Talman", serie="581634")
    ibanez1.save()

    return render(request, "AppGuitarras/ibanez.html")


#CRUD de Fender

def fenderFormulario(request):

    if request.method == "POST":

        formulario1 = FenderFormulario(request.POST)

        if formulario1.is_valid():

            info= formulario1.cleaned_data

            fenderguitarra = Fender(fenderguitarra=info["fenderguitarra"], serie=info["serie"])

            fenderguitarra.save()

            return render(request, "AppGuitarras/fender.html")

    else:

        formulario1 = FenderFormulario()
    

    return render(request, "AppGuitarras/fenderFormulario.html", {"form1":formulario1})

def busquedaFender(request):

    return render(request, "AppGuitarras/fender.html")

def resultadosFender(request):

    if request.GET["serie"]:

        serie = request.GET["serie"]
        fenderguitarra = Fender.objects.filter(serie__icontains=serie)

        return render(request, "AppGuitarras/fender.html", {"fenderguitarra":fenderguitarra, "serie": serie})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


#CRUD de Gibson

def gibsonFormulario(request):

    if request.method == "POST":

        formulario1 = GibsonFormulario(request.POST)

        if formulario1.is_valid():

            info= formulario1.cleaned_data

            gibsonguitarra = Gibson(gibsonguitarra=info["gibsonguitarra"], serie=info["serie"])

            gibsonguitarra.save()

            return render(request, "AppGuitarras/gibson.html")

    else:

        formulario1 = GibsonFormulario()
    

    return render(request, "AppGuitarras/gibsonFormulario.html", {"form1":formulario1})

def busquedaGibson(request):

    return render(request, "AppGuitarras/gibson.html")

def resultadosGbison(request):

    if request.GET["serie"]:

        serie = request.GET["serie"]
        gibsonguitarra = Gibson.objects.filter(serie__icontains=serie)

        return render(request, "AppGuitarras/gibson.html", {"gibsonguitarra":gibsonguitarra, "serie": serie})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


#CRUD de Ibanez

def ibanezFormulario(request):

    if request.method == "POST":

        formulario1 = IbanezFormulario(request.POST)

        if formulario1.is_valid():

            info= formulario1.cleaned_data

            ibanezguitarra = Ibanez(ibanezguitarra=info["ibanezguitarra"], serie=info["serie"])

            ibanezguitarra.save()

            return render(request, "AppGuitarras/ibanez.html")

    else:

        formulario1 = IbanezFormulario()
    

    return render(request, "AppGuitarras/ibanezFormulario.html", {"form1":formulario1})

def busquedaIbanez(request):

    return render(request, "AppGuitarras/ibanez.html")

def resultadosIbanez(request):

    if request.GET["serie"]:

        serie = request.GET["serie"]
        ibanezguitarra = Ibanez.objects.filter(serie__icontains=serie)

        return render(request, "AppGuitarras/ibanez.html", {"ibanezguitarra":ibanezguitarra, "serie": serie})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


#CRUD clases de Fender

class ListaFender(LoginRequiredMixin, ListView):

    model = Fender

class DetalleFender(LoginRequiredMixin, DetailView):

    model = Fender

class CrearFender(LoginRequiredMixin, CreateView):

    model = Fender
    success_url = "/AppGuitarras/fender/list" 
    fields = ["fenderguitarra", "Serie"]

class ActualizarFender(LoginRequiredMixin, UpdateView):

    model = Fender
    success_url = "/AppGuitarras/fender/list" 
    fields = ["fenderguitarra", "Serie"]

class BorrarFender(LoginRequiredMixin, DeleteView):

    model = Fender
    success_url = "/AppGuitarras/fender/list" 


#CRUD clases de Gibson

class ListaGibson(LoginRequiredMixin, ListView):

    model = Gibson

class DetalleGibson(LoginRequiredMixin, DetailView):

    model = Gibson

class CrearGibson(LoginRequiredMixin, CreateView):

    model = Gibson
    success_url = "/AppGuitarras/gibson/list" 
    fields = ["gibsonguitarra", "Serie"]

class ActualizarGibson(LoginRequiredMixin, UpdateView):

    model = Gibson
    success_url = "/AppGuitarras/gibson/list" 
    fields = ["gibsonguitarra", "Serie"]

class BorrarGibson(LoginRequiredMixin, DeleteView):

    model = Gibson
    success_url = "/AppGuitarras/gibson/list" 


#CRUD clases de Ibanez

class ListaIbanez(LoginRequiredMixin, ListView):

    model = Ibanez

class DetalleIbanez(LoginRequiredMixin, DetailView):

    model = Ibanez

class CrearIbanez(LoginRequiredMixin, CreateView):

    model = Ibanez
    success_url = "/AppGuitarras/ibanez/list" 
    fields = ["ibanezguitarra", "Serie"]

class ActualizarIbanez(LoginRequiredMixin, UpdateView):

    model = Ibanez
    success_url = "/AppGuitarras/ibanez/list" 
    fields = ["ibanezguitarra", "Serie"]

class BorrarIbanez(LoginRequiredMixin, DeleteView):

    model = Ibanez
    success_url = "/AppGuitarras/ibanez/list" 


#CRUD de usuarios

def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user =authenticate(username  =usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "AppGuitarras/inicio.html" , {"mensaje": f"Bienvenido {user}"})

        else:

            return render(request, "AppGuitarras/inicio.html", {"mensaje": "Datos Incorrectos."}) 

    else:

        form = AuthenticationForm() 

    return render(request, "AppGuitarras/login.html", {"formulario":form})


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppGuitarras/inicio.html", {"mensaje": "Usuario creado."})

    else:

        form = UsuarioRegistro()

    return render(request, "AppGuitarras/inicio.html", {"formulario":form})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppGuitarras/inicio.html")

    else:

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,

        })

    return render(request, "AppGuitarras/editarPerfil.html", {"formulkario":form, "usuario":usuario})


@login_required
def agregarAvatar(request):

    if request.method=="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["Imagen"])

            avatar.save()

            return render(request, "AppGuitarras/inicio.html")

    else:

        form = AvatarFormulario()

    return render(request, "AppGuitarras/agregarAvatar.html", {"formulario":form})
            



