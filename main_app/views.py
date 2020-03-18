from django.shortcuts import render

from .models import Finch

class Finch:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

finches = [
  Finch('Carmen', 'House', 'chirpy', 3),
  Finch('Sasha', 'Black Rosy', 'funny looking', 0),
  Finch('Hector', 'Java Sparrow', 'cool', 4)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })