from django.forms import ModelForm
from .models import Movies, Ticket, Club, ClubRep


class MovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class ticketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        #exclude = (' ',)

class AddClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'

class AddClubRepForm(ModelForm):
    class Meta:
        model = ClubRep
        fields = '__all__'
