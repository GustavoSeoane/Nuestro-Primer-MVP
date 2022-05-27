from django.shortcuts import render
from detalle.models import Detalle



# Create your views here.

def detallee (request):
    nuevo_familiar = Detalle.objects.create(
            name = "Olga",
            last_name = "Gonzalez",
            DNI = 45844486,
            fecha_nacimiento = "1980-12-15",
            email = "probando55@hotmail.com",
            Esta_Vivo = True,
            Observaciones = "Es la abuela"
            )
    context = {'nuevo_familiar' :nuevo_familiar}
    return render(request, 'detallee.html', context=context)


