import pyttsx3
from datetime import datetime
from models import Medicamento

class AssistenteVoz:
    """Responsável pela acessibilidade sonora do sistema."""
    
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150) 
        self.texto_completo = "" # Aqui nós criamos um "roteiro" vazio

    def adicionar_na_fila(self, texto):
        print(f"[Assistente de Voz]: {texto}") 
        # Em vez de mandar a voz falar, nós vamos colando as frases no roteiro
        self.texto_completo += texto + " "

    def reproduzir_tudo(self):
        # Manda a voz ler a história INTEIRA de uma vez só!
        if self.texto_completo.strip() != "":
            self.engine.say(self.texto_completo)
            self.engine.runAndWait()
            self.texto_completo = "" # Limpa o roteiro depois de falar

class GerenciadorSaude:
    """Controla a lista de remédios e avisa os horários."""
    
    def __init__(self):
        self.medicamentos = []
        self.voz = AssistenteVoz()

    def adicionar_medicamento(self, nome, dosagem, intervalo):
        novo_remedio = Medicamento(nome, dosagem, intervalo)
        self.medicamentos.append(novo_remedio)
        self.voz.adicionar_na_fila(f"O remédio {nome} foi cadastrado com sucesso.")

    def verificar_agenda(self):
        agora = datetime.now()
        self.voz.adicionar_na_fila("Verificando sua agenda de remédios para hoje.")
        
        for remedio in self.medicamentos:
            proxima = remedio.calcular_proxima_dose()
            
            if agora >= proxima:
                aviso = f"Está na hora de tomar o {remedio.nome}. A dosagem é de {remedio.dosagem}."
                self.voz.adicionar_na_fila(aviso)
                remedio.ultima_dose = agora
            else:
                tempo_restante = proxima - agora
                horas = int(tempo_restante.total_seconds() // 3600)
                minutos = int((tempo_restante.total_seconds() % 3600) // 60)
                self.voz.adicionar_na_fila(f"O remédio {remedio.nome} será em {horas} horas e {minutos} minutos.")

    def executar_falas(self):
        """Chama o motor de voz para falar tudo o que está pendente."""
        self.voz.reproduzir_tudo()