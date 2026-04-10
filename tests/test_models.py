import sys
import os
from datetime import datetime, timedelta

# Truque para o Python encontrar a pasta 'src' estando dentro da pasta 'tests'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models import Medicamento

def test_calcular_proxima_dose_remedio_novo():
    """Testa se um remédio sem 'ultima_dose' agenda a próxima para o momento atual."""
    remedio = Medicamento("Teste", "10mg", 8)
    proxima = remedio.calcular_proxima_dose()
    agora = datetime.now()
    
    # A diferença entre a 'proxima' e o 'agora' deve ser de menos de 1 segundo
    diferenca_segundos = abs((proxima - agora).total_seconds())
    assert diferenca_segundos < 1

def test_calcular_proxima_dose_com_historico():
    """Testa se a matemática de somar as horas do intervalo funciona corretamente."""
    agora = datetime.now()
    remedio = Medicamento("Teste", "10mg", 8, ultima_dose=agora)
    
    proxima = remedio.calcular_proxima_dose()
    esperado = agora + timedelta(hours=8)
    
    assert proxima == esperado