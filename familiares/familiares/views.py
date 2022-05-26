from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render # para vincular con la solapa de template1
from datetime import datetime


def saludoo (request):
    return HttpResponse ("<h1>Hola Gustavo, te dejo el entregable de la clase </h1>")

def fechaActual(request):
    fecha = datetime.now().date()
    mensaje = f"Hoy es {fecha}"
    return HttpResponse(mensaje)

# para vincular con la solapa de template1 - evitando poner la ruta. Hay que ajsutar setting Dir Base
def probando_Tem (request):
    context = {
        'Nombre' : 'Gustavo',
        'Apellido' : 'Seoane',
        'Edad' : '34',
        'Fecha_Nacimiento' : '08/07/1987',
        'Fecha' : datetime.now().date()
    }
    return render(request, 'template1.html', context = context)
