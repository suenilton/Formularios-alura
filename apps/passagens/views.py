from django.shortcuts import render
from passagens.forms import PassagemForm, PessoaForm

def index(request):
    form = PassagemForm()
    pessoaform = PessoaForm()

    dados = {
        'form': form,
        'pessoaform': pessoaform
    }

    return render(request, 'passagens\index.html', dados)

def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagemForm(request.POST)
        pessoaform = PessoaForm(request.POST)
    if form.is_valid():
        dados = {
            'form': form,
            'pessoaform': pessoaform
        }
        return render(request, 'passagens\minha_consulta.html', dados)
    else:
        print('Formulario inválido')
        dados = {
            'form': form,
            'pessoaform': pessoaform
        } 
        return render(request, 'passagens\index.html', dados)
