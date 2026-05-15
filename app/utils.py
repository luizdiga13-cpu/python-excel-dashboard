import os
from datetime import datetime


def criar_pasta(nome_pasta):

    """
    Cria uma pasta caso ela não exista.
    """

    if not os.path.exists(nome_pasta):
        os.makedirs(nome_pasta)


def data_atual():

    """
    Retorna data e hora atual.
    """

    return datetime.now().strftime(
        "%d/%m/%Y %H:%M"
    )


def salvar_upload(arquivo, caminho):

    """
    Salva arquivo enviado pelo usuário.
    """

    with open(caminho, "wb") as f:
        f.write(arquivo.getbuffer())