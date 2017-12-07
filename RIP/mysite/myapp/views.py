from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello fucking world!")


def base(request, username):
    return render(request, "base.html", {"username": username})


def index(request):
    listt = [{'name': 'die antwoord',
              'image': '/media/band1.jpg',
              },
             {'name': 'die antwoord2',
              'image': '',
              },
             {'name': 'die antwoord3',
              'image': '/media/band1.jpg',
              },
             {'name': 'die antwoord4',
              'image': '',
              },
             {'name': 'die antwoord',
              'image': '/media/band1.jpg',
              },
             ]
    return render(request, "index.html", {"list1": listt})
