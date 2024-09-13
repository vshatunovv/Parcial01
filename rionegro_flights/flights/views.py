from django.shortcuts import render, redirect
from .forms import FlightForm, Flight
from django.db.models import Count, Avg
# Create your views here.

def registrar_vuelos(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar vuelos')
    else:
        form=FlightForm()
    return render(request, 'registrar_vuelos.html', {'form': form})

def listar_vuelos (request):
    vuelos = Flight.objects.all().order_by('precio')
    return render (request,'listar_vuelos.html', {'vuelos': vuelos})


def estadisticas_vuelos(request):
    total_nacionales = Flight.objects.filter(tipo='Nacional').count()
    total_internacionales = Flight.objects.filter(tipo='Internacionales').count()
    promedio_nacionales= Flight.objects.filter(tipo='Nacional').aggregate(Avg('precio'))['precio__avg']
    return render (request, 'estadisticas_vuelos.html',{
        'total_nacionales': total_nacionales,
        'total_internacionales': total_internacionales,
        'promedio_nacionales': promedio_nacionales
    })
