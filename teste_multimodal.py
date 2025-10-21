from modelo_ia import AdamIAMultimodal

def teste_rapido():
    print("🚀 TESTE RÁPIDO ADAM MULTIMODAL")
    print("=" * 50)
    
    # Cria Adam
    adam = AdamIAMultimodal()
    
    # Tenta aprender
    if adam.aprender_tudo("dados"):
        print("\n✅ Aprendizado bem-sucedido!")
        
        # Treina
        if adam.treinar_modelo():
            print("✅ Modelo treinado!")
            
            # Testa perguntas
            perguntas = [
                "O que é Python?",
                "Fale sobre ciência",
                "O que você aprendeu?",
                "Quais tipos de arquivos você processou?"
            ]
            
            print("\n🧪 Testando perguntas:")
            for pergunta in perguntas:
                print(f"\n❓ {pergunta}")
                resposta = adam.responder_pergunta(pergunta)
                print(f"🤖 {resposta}")
                
            # Mostra estatísticas
            print(f"\n📊 Estatísticas:")
            stats = adam.get_estatisticas()
            for key, value in stats.items():
                print(f"   {key}: {value}")
                
        else:
            print("❌ Falha no treinamento")
    else:
        print("❌ Nenhum arquivo processado")

if __name__ == "__main__":
    teste_rapido()