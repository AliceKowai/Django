from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Reuniao
from reunioes.forms import ReuniaoForm

def index(request):
    reunioes = Reuniao.objects.all()
    return render(request, 'reunioes/index.html',{'reunioes': reunioes})

def register(request):
    if request.method == 'POST':
        form = ReuniaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reunião Marcada')
            form = ReuniaoForm()
        else:
            messages.error(request, 'Erro ao marcar')
    else: 
        form = ReuniaoForm()
    return render(request, 'reunioes/register.html',{'form': form})
    
def delete_reuniao(request, id):
    reuniao_marcada = Reuniao.objects.get(id = id)
    if request.method == 'POST':
        reuniao_marcada.delete()
        return redirect('/')
    return render(request, 'reunioes/delete.html')
