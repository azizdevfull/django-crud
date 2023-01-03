from django.shortcuts import render
from .models import Person
# Create your views here.
def home(request):
    people = Person.objects.all()
    return render(request, 'index.html', {"people": people})

def create(request):
    vname = request.POST.get('name')
    Person.objects.create(name=vname)
    people = Person.objects.all()
    return render(request, 'index.html', {"people": people})
    