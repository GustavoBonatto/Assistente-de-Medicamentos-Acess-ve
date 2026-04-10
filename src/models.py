from datetime import datetime, timedelta


class Medicamento:
    def __init__(self, nome, dosagem, intervalo_horas, ultima_dose=None):
        self.nome = nome
        self.dosagem = dosagem
        self.intervalo_horas = intervalo_horas
        self.ultima_dose = ultima_dose  # Agora aceita carregar uma data anterior

    def to_dict(self):
        """Converte o objeto para um dicionário (JSON)"""
        ultima_dose_texto = self.ultima_dose.isoformat() if self.ultima_dose else None

        return {
            "nome": self.nome,
            "dosagem": self.dosagem,
            "intervalo_horas": self.intervalo_horas,
            "ultima_dose": ultima_dose_texto
        }

    def calcular_proxima_dose(self):
        # Se nunca tomou, a próxima dose é agora
        if self.ultima_dose is None:
            return datetime.now()

        # Soma as horas de intervalo com a última vez que tomou
        return self.ultima_dose + timedelta(hours=self.intervalo_horas)
