from datetime import datetime, timedelta

class Medicamento:
    """Representa um medicamento e sua posologia."""
    
    def __init__(self, nome, dosagem, intervalo_horas):
        self.nome = nome
        self.dosagem = dosagem
        self.intervalo_horas = intervalo_horas
        self.ultima_dose = None

    def calcular_proxima_dose(self):
        # Se nunca tomou, a próxima dose é agora
        if self.ultima_dose is None:
            return datetime.now()
        
        # Soma as horas de intervalo com a última vez que tomou
        return self.ultima_dose + timedelta(hours=self.intervalo_horas)