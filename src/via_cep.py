import requests

def buscar_endereco_por_cep(cep: str):
    """
    Conecta à API pública ViaCEP para buscar dados do endereço do paciente.
    Realiza uma requisição HTTP GET conforme os requisitos do projeto.
    """
    # Remove traços ou espaços que o usuário possa digitar
    cep_limpo = "".join(filter(str.isdigit, str(cep)))
    
    if len(cep_limpo) != 8:
        return None
        
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
    
    try:
        # Faz a requisição HTTP GET para a API pública
        resposta = requests.get(url, timeout=5)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            # A API do ViaCEP retorna 'erro: true' se o CEP não existir
            if "erro" not in dados:
                return {
                    "rua": dados.get("logradouro"),
                    "bairro": dados.get("bairro"),
                    "cidade": dados.get("localidade"),
                    "estado": dados.get("uf")
                }
        return None
    except requests.RequestException:
        # Se a internet cair ou o site estiver fora do ar, retorna None de forma segura
        return None
    

if __name__ == "__main__":
    # Isso aqui só vai rodar se executarmos este arquivo diretamente
    print("Buscando CEP 01001-000 (Praça da Sé - SP)...")
    resultado = buscar_endereco_por_cep("01001000")
    print("Resultado encontrado:")
    print(resultado)