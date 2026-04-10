# 💊 Assistente de Medicamentos Acessível

Um assistente virtual em Python desenvolvido para ajudar pessoas (especialmente idosos ou com deficiência visual) a lembrarem dos horários de seus medicamentos através de alertas por voz.

## ✨ Funcionalidades
* **Cadastro de Remédios:** Registra o nome, dosagem e intervalo de horas.
* **Cálculo Automático:** Calcula exatamente o horário da próxima dose.
* **Alertas por Voz:** Utiliza a biblioteca `pyttsx3` para "falar" com o usuário.
* **Persistência de Dados:** Salva os medicamentos cadastrados em um arquivo `.json` automaticamente.

## 🚀 Tecnologias Utilizadas
* Python 3.10+
* `pyttsx3` (Text-to-Speech)
* `pytest` (Testes Automatizados)
* `flake8` (Linting / PEP 8)
* GitHub Actions (CI/CD)

## 🛠️ Como executar o projeto na sua máquina

1. Clone este repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/Assistente-de-Medicamentos-Acess-ve.git](https://github.com/SEU_USUARIO/Assistente-de-Medicamentos-Acess-ve.git)

2. Entre na pasta do projeto:
   ```bash
   cd Assistente-de-Medicamentos-Acess-ve

3. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
    # No Windows:
    .\venv\Scripts\activate 

4. Instale as dependências:
   ```bash
   pip install pyttsx3 pytest flake8

5. Execute o programa:
  ```bash
    cd src
    python main.py

🧪 Como rodar os testes e a formatação
   Para garantir que o código está funcionando e formatado corretamente, use os comandos abaixo na raiz do projeto:
   -Para testar a lógica matemática: pytest
   -Para verificar o estilo do código (PEP 8): flake8
