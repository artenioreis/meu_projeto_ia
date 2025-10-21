"""
Script completo para instalar todas as dependências
"""
import subprocess
import sys
import nltk

def instalar_dependencias():
    print("🚀 Instalando todas as dependências...")
    
    # Lista de pacotes para instalar
    pacotes = [
        'numpy',
        'scikit-learn', 
        'nltk',
        'flask'
    ]
    
    # Instala pacotes via pip
    for pacote in pacotes:
        try:
            print(f"📦 Instalando {pacote}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
            print(f"✅ {pacote} instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao instalar {pacote}: {e}")
    
    # Baixa recursos do NLTK
    print("\n📥 Baixando recursos do NLTK...")
    recursos_nltk = ['punkt_tab', 'punkt', 'stopwords']
    
    for recurso in recursos_nltk:
        try:
            nltk.download(recurso, quiet=True)
            print(f"✅ Recurso {recurso} baixado!")
        except Exception as e:
            print(f"⚠️  Não foi possível baixar {recurso}: {e}")
    
    print("\n🎉 Todas as dependências foram instaladas!")
    print("👉 Agora você pode executar: python app.py")

if __name__ == "__main__":
    instalar_dependencias()