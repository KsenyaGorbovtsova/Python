from django import forms
from .models import Band
from django.forms import extras
FORM_ERROR_MESSAGES = {'required': 'Пожалуйста, заполните это поле'}
class BandAddingForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name',
                                                         'class': 'form-control', }),
                           max_length=20)

    origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Origin',
                                                         'class': 'form-control', }),
                           max_length=50)
    genre = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Genre',
                                                           'class': 'form-control', }),
                             max_length=20)
    founding_date = forms.DateField(
    widget=extras.SelectDateWidget(
        empty_label=("Choose Year", "Choose Month", "Choose Day"),
    ),
)

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Description',
                                                               'rows': 6,
                                                               'id': 'descriptionArea',
                                                               'oninput': 'productDescriptionValidate(event)',
                                                               'onblur': 'removeDescriptionTipOnBlur()',
                                                               'onfocus': 'productDescriptionValidate(event)'}))
    image = forms.ImageField(required=False)


    def add_product(self):
        name = self.cleaned_data['name']
        origin = self.cleaned_data['origin']
        genre = self.cleaned_data['genre']
        founding_date = self.cleaned_data['founding_date']
        description = self.cleaned_data['description']
        image = self.cleaned_data['image']


        try:

            if image:
                new_band = Band(name=name, origin=origin, genre=genre, founding_date=founding_date,
                                      description=description, image=image)
            else:
                new_band = Band(name=name, origin=origin,genre=genre, founding_date=founding_date,
                                      description=description)
            new_band.save()


            return new_band.id
        except BaseException as e:  # если вдруг что-то пошло не так
            print(e)
            return False

