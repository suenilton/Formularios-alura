from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipo_de_classe
from passagens.validation import *

class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do Vôo', choices=tipo_de_classe)
    informacoes = forms.CharField(
        label='Informações',
        max_length=200, 
        required=False,
        widget=forms.Textarea()
    )
    email = forms.EmailField(label='Email', max_length=150, required=True)
    
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        print(type(data_ida))
        lista_de_erros = {}
        origem_igual_destino(origem, destino, lista_de_erros)
        campo_contem_numero(origem, 'origem', lista_de_erros)
        campo_contem_numero(destino, 'destino', lista_de_erros)
        valida_data(data_ida, data_volta, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data