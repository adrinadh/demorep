from django.shortcuts import render

# Create your views here.
# tasks/views.py
from .models import Place, Team
from django.shortcuts import render


# def inputs(request):
#     return render(request, 'inputs.html')


# def result(request):
#     num1 = int(request.GET.get('num1', 0))
#     num2 = int(request.GET.get('num2', 0))
#     add = num1 + num2
#     sub = num1 - num2
#     mul = num1 * num2
#     div = num1 / num2

#     context = {'add': add, 'sub': sub, 'mul': mul, 'div': div}
#     return render(request, 'results.html', context)

# -------------------------------------------------------------------------------------

def index(request):
    objPlace = Place.objects.all()
    objTeam = Team.objects.all()
    return render(request, 'index.html', {'resultPlace': objPlace, 'resultTeam': objTeam})
