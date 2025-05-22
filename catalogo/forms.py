from django import forms
from .models import MudaPlantada

class MudaPlantadaForm(forms.ModelForm):
    class Meta:
        model = MudaPlantada
        fields = ['especie', 'data_plantio', 'quantidade']