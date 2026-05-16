from services import GerenciadorSaude
from via_cep import buscar_endereco_por_cep  # <-- Importamos a nossa nova ferramenta aqui!

if __name__ == "__main__":
    # --- NOVA PARTE: CADASTRO DO PACIENTE COM API ---
    print("--- 👤 Perfil do Paciente ---")
    nome = input("Digite o nome do paciente: ")
    cep = input("Digite o CEP do paciente (apenas números): ")

    print("Buscando endereço na internet...")
    endereco = buscar_endereco_por_cep(cep)

    if endereco:
        print(f"✅ Sucesso! Paciente {nome} reside em: {endereco['rua']}, {endereco['cidade']} - {endereco['estado']}\n")
    else:
        print("❌ Aviso: Não foi possível encontrar o endereço ou o sistema está offline.\n")

    print("--- Iniciando a lista de remedios ---")

    app = GerenciadorSaude()

    app.adicionar_medicamento("Paracetamol", "500 miligramas", 8)
    app.adicionar_medicamento("Vitamina D", "uma gota", 24)

    print("\n--- Iniciando a Verificação ---\n")

    app.verificar_agenda()

    app.executar_falas()
