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
def choice(request):

    return render(request, "choice.html")
"""def index(request):
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
    return render(request, "index.html", {"list1": listt})"""

from .models import Band, Artist
class Extra(View):
    template_name='extra.html'
    def get(self, request, band_id):
        bands=Band.objects.get(id=band_id)
        artists=Artist.objects.filter(band=bands)



        data = {
            'bands' : bands,
            'artist' : artists,
            'auth': request.user.is_authenticated,
            'user': request.user,

        }
        return render(request, self.template_name, data)


from django.views.generic.list import ListView

from myapp import models

class PrivateBandList(ListView):

    model= models.Band
    paginate_by = 6
    context_object_name = 'band'
    template_name = 'index.html'


    def get_context_data(self):
        context = super(PrivateBandList, self).get_context_data()
        context['band_adding_form'] = BandAddingForm()
        return context

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
@login_required
def choice(request):
    return render(request, 'choice.html')
def signup(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        if form1.is_valid():
            form1.save()
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('choice')
    else:
        form1 = UserCreationForm()
    return render(request, 'modal_window.html', {'form1': form1})

from .forms import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

class BandAddingView(View):
    band_adding_form_class = BandAddingForm

    def post(self, request):
        form = self.band_adding_form_class(request.POST, request.FILES)
        if form.is_valid():
            new_band_id = form.add_product()
            if new_band_id:
                url = reverse('index')
                return HttpResponseRedirect(url)
            else:
                return HttpResponseRedirect('/error/')
        else:
            return HttpResponseRedirect('/index/')


class ErrorView(View):
    template_name = 'error.html'

    def get(self, request):
        data = {'user': request.user,
                'auth': request.user.is_authenticated}
        return render(request, self.template_name, data)