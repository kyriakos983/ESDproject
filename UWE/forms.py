from django.forms import ModelForm
from .models import Movies, ticket, Club


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class ticketForm(ModelForm):
    class Meta:
        model = ticket
        fields = '__all__'
        #exclude = (' ',)

class AddClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'


