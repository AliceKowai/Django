from django.shortcuts import render
from atracoes_turisticas.models import AtracaoTuristica
from atracoes_turisticas.forms import AtracaoTuristicaForm
from django.contrib import messages


def index(request):
    atracao_turisticas = AtracaoTuristica.objects.all()
    return render(request, 'atracoes_turisticas/index.html',{'atracoes_turisticas': atracao_turisticas})

def register(request):
    if request.method == 'POST':
        form = AtracaoTuristicaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ponto Turistico Cadastrado')
            form = AtracaoTuristicaForm()
        else:
            messages.error(request, 'Erro ao cadastrar')
    else: 
        form = AtracaoTuristicaForm()
    return render(request, 'atracoes_turisticas/register.html',{'form': form})
    
