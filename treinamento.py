from modelo_ia import AdamIAMultimodal
import os

def treinar_adam():
    """
    Função principal para treinar a Adam Multimodal
    """
    print("🎯 Iniciando treinamento da Adam Multimodal...")
    
    # Cria uma nova instância da Adam
    adam = AdamIAMultimodal()
    
    # Adam aprende com TODOS os arquivos automaticamente
    if adam.aprender_tudo("dados"):
        # Treina o modelo
        if adam.treinar_modelo():
            print("🎉 Adam Multimodal treinada com sucesso!")
            return adam
        else:
            print("❌ Falha no treinamento da Adam!")
            return None
    else:
        print("❌ Adam não encontrou conhecimento para aprender!")
        return None

# Alias para compatibilidade
treinar_ia = treinar_adam