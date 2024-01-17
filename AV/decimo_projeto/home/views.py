from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages

def index(request):
    return render(request, 'home/index.html')
def contato(request):
    form = ContatoForm(request.POST)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            print('Mensagem Enviada')
            print(f'Nome: {nome}')
            print(f'email: {email}')
            print(f'assunto: {assunto}')
            print(f'mensagem: {mensagem}')

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar sua mensagem!')

    context = {
        'form': form
    }

    return render(request, 'home/contato.html', context)

def produto (request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            print(f'nome: {prod.nome}')
            print(f'preco: {prod.nome_produto}')
            print(f'Imagem: {prod.imagem_produto}')

            messages.success(request, 'Produto cadastrado com sucesso')
        else:
            messages.error(request, 'Erro ao cadastrar o produto')
    else:
        form = ProdutoModelForm()
    context = {
        'form' : form
    }
    return render(request, 'home/produto.html', context)
