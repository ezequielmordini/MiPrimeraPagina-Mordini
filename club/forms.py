from django import forms
from .models import Jugador, Partido, Noticia, Socio

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'

class BusquedaJugadorForm(forms.Form):
    nombre = forms.CharField(label='Nombre del jugador', max_length=100)

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'email', 'dni', 'fecha_nacimiento', 'direccion']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }

