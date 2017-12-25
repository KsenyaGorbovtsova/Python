from django.shortcuts import render
from django.views import View
# Create your views here.
from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello fucking world!")


def base(request, username):
    return render(request, "base.html", {"username": username})

def main(request):
    form1 = UserCreationForm(request.POST)
    form = AuthenticationForm(request.POST)
    context = {'form1': form1, 'form': form, }
    return render(request, "main.html", context)
def index(request):
    listt = [{'id':'1',
              'name': 'die antwoord',
              'image': 'band1.jpg',
              },
             {'name': 'die antwoord2',
              'image': '',
              'id': '2',
              },
             {'name': 'die antwoord3',
              'image': 'band1.jpg',
              'id': '3',
              },
             {'name': 'die antwoord4',
              'image': '',
              'id': '4',
              },

             ]
    return render(request, "index.html", {"list1": listt})


class Extra(View):
    def get(self, request, id):
        data = {
            'item': {
                'id': id,
            }
        }
        return render(request, "extra.html", data)


from django.views.generic.list import ListView

from myapp import models
class PrivateBandList(ListView):

    model= models.Band
    paginate_by = 10
    context_object_name = 'band'
    template_name = 'index.html'


from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    return render(request, 'index.html')
def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form1 = UserCreationForm()
    return render(request, 'modal_window.html', {'form1': form1})

