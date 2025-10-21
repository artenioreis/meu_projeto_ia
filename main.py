from treinamento import treinar_ia
from modelo_ia import IAApprendiz
import os

def mostrar_menu():
    """
    Mostra o menu de opções
    """
    print("\n" + "="*50)
    print("🤖 IA DE APRENDIZADO - MENU PRINCIPAL")
    print("="*50)
    print("1. 🗣️  Fazer uma pergunta")
    print("2. 📚 Adicionar novo conhecimento")
    print("3. ℹ️   Ver informações da IA")
    print("4. 🚪 Sair")
    print("="*50)

def main():
    """
    Função principal do programa
    """
    print("Bem-vindo à IA de Aprendizado!")
    print("Iniciando treinamento...")
    
    # Treina a IA
    ia = treinar_ia()
    
    if ia is None:
        print("Não foi possível inicializar a IA. Verifique se há arquivos na pasta 'dados/'")
        return
    
    # Loop principal do programa
    while True:
        mostrar_menu()
        
        opcao = input("\n📝 Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            # Opção: Fazer pergunta
            pergunta = input("\n❓ Faça sua pergunta: ").strip()
            
            if pergunta:
                resposta = ia.responder_pergunta(pergunta)
                print(f"\n🤖 Resposta: {resposta}")
            else:
                print("⚠️  Por favor, digite uma pergunta!")
        
        elif opcao == "2":
            # Opção: Adicionar conhecimento
            novo_conhecimento = input("\n📝 Digite o novo conhecimento: ").strip()
            
            if novo_conhecimento:
                ia.adicionar_conhecimento(novo_conhecimento)
                print("✅ Conhecimento adicionado com sucesso!")
            else:
                print("⚠️  Por favor, digite algum conteúdo!")
        
        elif opcao == "3":
            # Opção: Ver informações
            print(f"\n📊 INFORMAÇÕES DA IA:")
            print(f"   • Sentenças aprendidas: {len(ia.respostas)}")
            print(f"   • Modelo treinado: {'✅ Sim' if ia.caracteristicas is not None else '❌ Não'}")
        
        elif opcao == "4":
            # Opção: Sair
            print("\n👋 Obrigado por usar a IA! Até logo!")
            break
        
        else:
            print("❌ Opção inválida! Escolha entre 1 e 4.")

# Executa o programa
if __name__ == "__main__":
    main()