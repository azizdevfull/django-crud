from django.shortcuts import render, redirect
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

def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'update.html', {"person": person})

def update(request, id):
    vname = request.POST.get('name')
    person = Person.objects.get(id=id)
    person.name = vname
    person.save()
    return redirect(home)
    
    
    