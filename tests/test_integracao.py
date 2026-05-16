import sys
import os

# Adiciona a pasta raiz do projeto ao caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.via_cep import buscar_endereco_por_cep  # noqa: E402


def test_integracao_api_viacep_retorna_endereco_valido():
    """
    Testa se a API do ViaCEP está respondendo corretamente.
    Busca o CEP da Praça da Sé (01001-000) e valida a resposta.
    """
    resultado = buscar_endereco_por_cep("01001000")

    # Verifica se a API não retornou vazio (None)
    assert resultado is not None

    # Verifica se a rua retornada é realmente a Praça da Sé
    assert resultado["rua"] == "Praça da Sé"
    assert resultado["estado"] == "SP"


def test_integracao_api_viacep_retorna_none_para_cep_invalido():
    """
    Testa como o sistema lida com um CEP que não existe (ex: 00000-000)
    """
    resultado = buscar_endereco_por_cep("00000000")
    assert resultado is None
