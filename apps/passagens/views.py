from django.shortcuts import render
from passagens.forms import PassagemForm

def index(request):
    form = PassagemForm()

    dados = {
        'form': form
    }

    return render(request, 'passagens\index.html', dados)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
    if form.is_valid():
        dados = {
            'form': form
        }
        return render(request, 'passagens\minha_consulta.html', dados)
    else:
        print('Formulario inválido')
        dados = {
            'form': form
        } 
        return render(request, 'passagens\index.html', dados)
