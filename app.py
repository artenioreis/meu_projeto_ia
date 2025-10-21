from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

print("🚀 INICIANDO ADAM IA...")

# Inicializa a aplicação Flask
app = Flask(__name__)
app.secret_key = 'adam_ia_super_inteligente_2024'

# Tenta importar a Adam
try:
    from modelo_ia import AdamIA
    from treinamento import treinar_adam
    ADAM_DISPONIVEL = True
    print("✅ Módulos da Adam carregados com sucesso!")
except ImportError as e:
    print(f"❌ Erro ao carregar módulos: {e}")
    ADAM_DISPONIVEL = False

# Instância global da Adam
adam = None

def inicializar_adam():
    """
    Inicializa a Adam
    """
    global adam
    if not ADAM_DISPONIVEL:
        print("❌ Módulos da Adam não disponíveis")
        return None
    
    try:
        print("🤖 Inicializando Adam...")
        adam = treinar_adam()
        if adam:
            stats = adam.get_estatisticas()
            print(f"✅ Adam inicializada! Conhecimento: {stats['total_sentencas']} sentenças")
            return adam
        else:
            print("❌ Falha ao treinar Adam")
            return None
    except Exception as e:
        print(f"❌ Erro na inicialização: {e}")
        return None

# Inicializa a Adam
adam = inicializar_adam()

@app.route('/')
def index():
    """Página inicial"""
    print("📄 Acessando página inicial...")
    return render_template('index.html')

@app.route('/chat')
def chat():
    """Página do chat"""
    print("💬 Acessando chat...")
    return render_template('chat.html')

@app.route('/api/perguntar', methods=['POST'])
def perguntar():
    """API para perguntas"""
    try:
        data = request.get_json()
        pergunta = data.get('pergunta', '').strip()
        
        print(f"❓ Pergunta recebida: {pergunta}")
        
        if not pergunta:
            return jsonify({
                'sucesso': False,
                'resposta': '❌ Por favor, digite uma pergunta!'
            })
        
        if adam is None:
            return jsonify({
                'sucesso': False,
                'resposta': '🤖 Adam não está disponível no momento.'
            })
        
        resposta = adam.responder_pergunta(pergunta)
        print(f"🤖 Resposta: {resposta[:50]}...")
        
        return jsonify({
            'sucesso': True,
            'resposta': resposta,
            'pergunta': pergunta
        })
        
    except Exception as e:
        print(f"❌ Erro na API: {e}")
        return jsonify({
            'sucesso': False,
            'resposta': f'❌ Erro: {str(e)}'
        })

@app.route('/api/info')
def get_info():
    """API para informações"""
    if adam is None:
        return jsonify({
            'nome': 'Adam - Em inicialização',
            'status': 'Inicializando...',
            'total_sentencas': 0,
            'total_arquivos': 0,
            'modelo_treinado': False
        })
    
    try:
        stats = adam.get_estatisticas()
        return jsonify(stats)
    except:
        return jsonify({
            'nome': 'Adam - Disponível',
            'status': 'Operacional',
            'total_sentencas': 'Carregando...',
            'total_arquivos': 'Carregando...',
            'modelo_treinado': True
        })

@app.route('/health')
def health_check():
    """Health check"""
    return jsonify({
        'status': 'online',
        'adam': adam is not None,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/debug')
def debug():
    """Página de debug"""
    info = {
        'flask_working': True,
        'adam_loaded': adam is not None,
        'templates_exist': os.path.exists('templates'),
        'static_exist': os.path.exists('static'),
        'dados_exist': os.path.exists('dados')
    }
    return jsonify(info)

if __name__ == '__main__':
    print("\n🎉 SERVIDOR PRONTO!")
    print("📍 URLs disponíveis:")
    print("   • http://localhost:5000/          - Página inicial")
    print("   • http://localhost:5000/chat      - Chat com Adam")
    print("   • http://localhost:5000/health    - Health check")
    print("   • http://localhost:5000/debug     - Debug info")
    print("   • http://localhost:5000/api/info  - Info da Adam")
    print("\n🚀 Iniciando servidor...")
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)