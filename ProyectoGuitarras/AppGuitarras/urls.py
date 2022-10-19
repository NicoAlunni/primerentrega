from django.urls import path, include
from AppGuitarras.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path("", inicio, name="Inicio"),
    path("fender/", fender, name="Fender"),
    path("gibson/", gibson, name="Gibson"),
    path("ibanez/", ibanez, name="Ibanez"),
    

    #CRUD de Fender

    path("fenderFormulario/", fenderFormulario, name="FormularioFender"),
    path("fenderResultados/", resultadosFender, name= "resultadosFender"),
    path("fenderBuscar/", busquedaFender, name="BuscandoFender"),

    #CRUD de Gibson

    path("gibsonFormulario/", gibsonFormulario, name="FormularioGibson"),
    path("gibsonResultados/", resultadosGbison, name= "ResultadosGibson"),
    path("gibsonBuscar/", busquedaGibson, name="BuscandoGibson"),

    #CRUD de Ibanez

    path("ibanezFormulario/", ibanezFormulario, name="FormularioIbanez"),
    path("ibanezResultados/", resultadosIbanez, name= "resultadosIbanez"),
    path("ibanezBuscar/", busquedaIbanez, name="BuscandoIbanez"),

    #CRUD de Fender usando clases

    path("fender/list/", ListaFender.as_view(), name="FenderLeer"),
    path("fender/<int:pk>", DetalleFender.as_view(), name="FenderDetalle"),
    path("fender/crear/", CrearFender.as_view(), name="FenderCrear"),
    path("fender/editar/<int:pk>", ActualizarFender.as_view(), name="FenderEditar"),
    path("fender/borrar/<int:pk>", BorrarFender.as_view(), name="FenderBorrar"),

    #CRUD de Gibson usando clases

    path("gibson/list/", ListaGibson.as_view(), name="GibsonLeer"),
    path("gibson/<int:pk>", DetalleGibson.as_view(), name="GibsonDetalle"),
    path("gibson/crear/", CrearGibson.as_view(), name="GibsonCrear"),
    path("gibson/editar/<int:pk>", ActualizarGibson.as_view(), name="GibsonEditar"),
    path("gibson/borrar/<int:pk>", BorrarGibson.as_view(), name="GibsonBorrar"),

    #CRUD de Ibanez usando clases

    path("ibanes/list/", ListaIbanez.as_view(), name="IbanezLeer"),
    path("ibanez/<int:pk>", DetalleIbanez.as_view(), name="IbanezDetalle"),
    path("ibanez/crear/", CrearIbanez.as_view(), name="IbanezCrear"),
    path("ibanez/editar/<int:pk>", ActualizarIbanez.as_view(), name="IbanezEditar"),
    path("ibanez/borrar/<int:pk>", BorrarIbanez.as_view(), name="IbanezBorrar"),


    #CRUD de sesion

    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="SignUp"),
    path("logout/", LogoutView.as_view(template_name="AppGuitarras/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar")



    ]
