from django.shortcuts import render
from .models import MudaPlantada

def mudas_disponiveis(request):
    mudas = MudaPlantada.objects.select_related('especie').all()
    for muda in mudas:
        muda.data_muda = muda.previsao_muda()
        muda.data_flor = muda.previsao_flor()
    return render(request, 'catalogo/mudas.html', {'mudas': mudas})


from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import MudaPlantadaForm  # vamos criar esse form
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def cadastrar_muda(request):
    if request.method == "POST":
        form = MudaPlantadaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")  # redireciona de volta à página inicial
    else:
        form = MudaPlantadaForm()
    return render(request, "catalogo/cadastrar_muda.html", {"form": form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST

@require_POST
@login_required
def deletar_muda(request, muda_id):
    muda = get_object_or_404(MudaPlantada, id=muda_id)
    muda.delete()
    return redirect("/")

@login_required
def editar_muda(request, muda_id):
    muda = get_object_or_404(MudaPlantada, id=muda_id)
    if request.method == 'POST':
        form = MudaPlantadaForm(request.POST, instance=muda)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MudaPlantadaForm(instance=muda)
    return render(request, 'catalogo/editar_muda.html', {'form': form, 'muda': muda})