import subprocess
import sys
import nltk

def instalar_dependencias():
    print("🚀 Instalando dependências para Adam Multimodal...")
    
    pacotes = [
        'numpy',
        'scikit-learn', 
        'nltk',
        'flask',
        'python-docx',
        'PyPDF2',
        'pdfplumber',
        'openpyxl',
        'python-pptx',
        'odfpy',
        'SpeechRecognition',
        'pydub',
        'moviepy',
        'pillow',
        'textract'
    ]
    
    for pacote in pacotes:
        try:
            print(f"📦 Instalando {pacote}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pacote])
            print(f"✅ {pacote} instalado!")
        except subprocess.CalledProcessError as e:
            print(f"⚠️  Erro ao instalar {pacote}: {e}")
    
    # Baixa recursos do NLTK
    print("\n📥 Baixando recursos do NLTK...")
    nltk.download('punkt_tab', quiet=True)
    
    print("\n🎉 Adam Multimodal está pronta!")
    print("👉 Adicione arquivos na pasta 'dados/' e execute: python app.py")

if __name__ == "__main__":
    instalar_dependencias()