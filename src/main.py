from services import GerenciadorSaude

if __name__ == "__main__":
    print("--- Iniciando a lista de remedios ---")

    app = GerenciadorSaude()

    app.adicionar_medicamento("Paracetamol", "500 miligramas", 8)
    app.adicionar_medicamento("Vitamina D", "uma gota", 24)

    print("\n--- Iniciando a Verificação ---\n")

    app.verificar_agenda()

    # O toque mágico: Faz o assistente reproduzir todas as falas acumuladas
    app.executar_falas()
