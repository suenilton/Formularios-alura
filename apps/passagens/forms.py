from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipo_de_classe

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