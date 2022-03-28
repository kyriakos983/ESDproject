from django.forms import ModelForm
from UWE.views import Movies


class addmovieForm(ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'
