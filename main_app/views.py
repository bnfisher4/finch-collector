from django.shortcuts import render

from django.http import HttpResponse

class Finch:
  def __init__(self, name, species, description, age):
    self.name = name
    self.species = species
    self.description = description
    self.age = age

finches = [
  Finch('Carmen', 'house', 'chirpy', 3),
  Finch('Sasha', 'black rosy', 'funny looking', 0),
  Finch('Hector', 'java sparrow', 'cool', 4)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })