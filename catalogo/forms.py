from django import forms
from .models import MudaPlantada

class MudaPlantadaForm(forms.ModelForm):
    class Meta:
        model = MudaPlantada
        fields = ['especie', 'data_plantio', 'quantidade']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordena as espécies alfabeticamente pelo nome
        self.fields['especie'].queryset = Especie.objects.order_by('nome')