def origem_igual_destino(origem, destino, lista_de_erros):
    """Verifica se o destino é igual a Origem"""

    if origem == destino:
        lista_de_erros['destino'] = 'Os campos de origem e destino não podem ser iguais.'

def campo_contem_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se o campo passado por parâmetro não contém números."""

    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'O campo não pode conter números'

def valida_data(data_ida, data_volta, data_pesquisa, lista_de_erros):
    """Valida se a data de ida é menor que a data de volta e maior ou igual a data de hoje."""

    if data_ida > data_volta:
        lista_de_erros['data_volta'] = 'A data de volta deve ser posterior a data de ida.'

    if data_ida < data_pesquisa:
        lista_de_erros['data_ida'] = 'A data de ida não pode ser anterior a data de hoje.'