🤖 Adam - IA Multimodal de Aprendizado
<div align="center">
    
https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/Flask-2.3+-green.svg
https://img.shields.io/badge/Machine%2520Learning-Scikit--learn-orange.svg
https://img.shields.io/badge/NLP-NLTK-yellow.svg
https://img.shields.io/badge/Multimodal-IA-purple.svg


Uma inteligência artificial que aprende automaticamente com múltiplos tipos de arquivos

Características • Instalação • Uso • Formatos Suportados • API • Estrutura

</div>
🌟 Sobre o Projeto
A Adam é uma IA de aprendizado multimodal que processa automaticamente diversos tipos de arquivos para construir seu conhecimento. Ela utiliza Processamento de Linguagem Natural (NLP) e algoritmos de similaridade para responder perguntas baseadas no conteúdo aprendido.

🎯 Destaques
✅ Aprendizado Automático - Aprende com qualquer arquivo na pasta dados/

🔄 Processamento Multimodal - Suporte a documentos, áudio, vídeo e mais

🎨 Interface Web - Interface intuitiva com Flask

🧠 NLP Avançado - Usa TF-IDF e similaridade de cosseno

📊 Estatísticas Detalhadas - Monitoramento do conhecimento adquirido

🚀 Características
📁 Formatos Suportados
Categoria	Formatos	Descrição
📄 Documentos	.txt, .docx, .pdf, .rtf, .odt	Processamento de texto completo
📊 Planilhas	.xlsx, .xls	Extração de dados de células
🎤 Apresentações	.pptx, .ppt	Texto de slides e notas
🎵 Áudio	.mp3, .wav, .aac, .wma, .ogg	Transcrição automática
🎬 Vídeo	.mp4, .avi, .mov, .mkv, .wmv	Extração e transcrição de áudio
🧠 Capacidades da IA
Aprendizado Automático: Processa automaticamente todos os arquivos

Busca Semântica: Encontra respostas baseadas no significado

Respostas Contextuais: Fornece respostas baseadas no conhecimento aprendido

Atualização em Tempo Real: Aprende novos arquivos sem reiniciar

Estatísticas Detalhadas: Monitora progresso e tipos processados

📦 Instalação
Pré-requisitos

1. Clone o Repositório
git clone https://github.com/seu-usuario/adam-ia-multimodal.git
cd adam-ia-multimodal

2. Crie um Ambiente Virtual (Recomendado)
bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows
3. Instale as Dependências
bash
pip install -r requirements.txt
4. Instalação Automática (Recomendado)
bash
python instalar_multimodal.py
🎮 Uso
Iniciar a Adam
bash
python app.py
Acesse a interface web: http://localhost:5000

Uso Rápido via Terminal
bash
python teste_multimodal.py
Estrutura Básica
text
meu_projeto_ia/
├── 📁 dados/                 # Pasta com arquivos para aprender
├── 📁 templates/            # Interface web
├── 📁 static/              # CSS, JavaScript
├── app.py                  # Aplicação principal Flask
├── modelo_ia.py           # Classe Adam Multimodal
├── treinamento.py         # Sistema de treinamento
└── requirements.txt       # Dependências
📁 Formatos Suportados
Documentos de Texto
.txt: Arquivos de texto simples

.docx: Documentos Microsoft Word

.pdf: Documentos PDF (extração de texto)

.rtf: Rich Text Format

.odt: OpenDocument Text

Planilhas
.xlsx, .xls: Microsoft Excel

Extrai texto de todas as células

Apresentações
.pptx, .ppt: Microsoft PowerPoint

Extrai texto de slides e notas

Arquivos de Áudio
.mp3, .wav, .aac, .wma, .ogg

Transcrição automática para texto

Arquivos de Vídeo
.mp4, .avi, .mov, .mkv, .wmv

Extrai áudio e transcreve para texto

🔧 API
Endpoints Disponíveis
Método	Endpoint	Descrição
GET	/	Página inicial com dashboard
GET	/chat	Interface de chat com a Adam
POST	/api/perguntar	Fazer perguntas à Adam
POST	/api/adicionar_conhecimento	Adicionar conhecimento manual
GET	/api/info	Informações da Adam
POST	/api/recarregar	Recarregar conhecimento
GET	/health	Status do servidor
GET	/debug	Informações de debug
Exemplo de Uso da API
python
import requests

# Fazer uma pergunta
response = requests.post('http://localhost:5000/api/perguntar', 
    json={'pergunta': 'O que é Python?'}
)
print(response.json())

# Obter informações
response = requests.get('http://localhost:5000/api/info')
print(response.json())
🏗️ Estrutura do Projeto
text
adam-ia-multimodal/
├── 📁 dados/                     # Arquivos para aprendizado
│   ├── 📄 documentos/
│   ├── 🎵 audios/
│   ├── 🎬 videos/
│   └── 📊 planilhas/
├── 📁 src/                       # Código fonte
│   ├── app.py                   # Aplicação Flask
│   ├── modelo_ia.py            # Classe AdamIA Multimodal
│   ├── treinamento.py          # Sistema de treinamento
│   └── 📁 utils/               # Utilitários
├── 📁 templates/               # Templates HTML
│   ├── base.html
│   ├── index.html
│   └── chat.html
├── 📁 static/                  # Arquivos estáticos
│   ├── 📁 css/
│   ├── 📁 js/
│   └── 📁 images/
├── 📁 tests/                   # Testes
├── requirements.txt            # Dependências
├── instalar_multimodal.py     # Script de instalação
├── teste_multimodal.py        # Teste rápido
└── README.md                  # Este arquivo
🧩 Exemplos de Uso
1. Aprendizado Automático
python
from modelo_ia import AdamIAMultimodal

# Cria a Adam
adam = AdamIAMultimodal()

# Aprende com todos os arquivos
adam.aprender_tudo("dados")

# Treina o modelo
adam.treinar_modelo()

# Faz perguntas
resposta = adam.responder_pergunta("O que é machine learning?")
print(resposta)
2. Adicionar Conhecimento Manual
python
# Adiciona conhecimento manualmente
adam.adicionar_conhecimento(
    "Python é uma linguagem de programação de alto nível muito usada em ciência de dados e machine learning.",
    fonte="Conhecimento Manual"
)
3. Estatísticas
python
# Obtém estatísticas
stats = adam.get_estatisticas()
print(f"Arquivos processados: {stats['total_arquivos']}")
print(f"Sentenças aprendidas: {stats['total_sentencas']}")
print(f"Tipos processados: {stats['tipos_processados']}")
🔍 Funcionamento Técnico
Arquitetura
Processamento Multimodal: Detecta e processa diferentes tipos de arquivos

Extração de Texto: Converte conteúdo para texto uniforme

Pré-processamento: Limpeza e tokenização do texto

Vetorização TF-IDF: Converte texto em representações numéricas

Similaridade de Cosseno: Encontra respostas mais relevantes

Interface Web: Disponibiliza via Flask

Algoritmos
TF-IDF (Term Frequency-Inverse Document Frequency): Para vetorização de texto

Similaridade de Cosseno: Para encontrar respostas relevantes

NLTK: Para processamento de linguagem natural

Processadores Especializados: Para cada tipo de arquivo

🐛 Solução de Problemas
Problemas Comuns
Arquivos não são processados

Verifique se estão na pasta dados/

Confirme que o formato é suportado

Verifique permissões de leitura

Erro de codificação

A Adam tenta múltiplas codificações automaticamente

Para arquivos problemáticos, converta para UTF-8

Processamento lento de áudio/vídeo

Arquivos grandes podem demorar

Use arquivos menores para teste

Dependências faltando

Execute python instalar_multimodal.py novamente

Verifique se todas as bibliotecas foram instaladas

Logs e Debug
bash
# Verifique os logs no terminal
python app.py

# Ou use o endpoint de debug
curl http://localhost:5000/debug
🤝 Contribuindo
Contribuições são bem-vindas! Siga estos passos:

Fork o projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

Áreas para Melhoria
Suporte a mais formatos de arquivo

Processamento em lote assíncrono

Cache de modelos treinados

Interface administrativa

Análise de sentimentos

Suporte a múltiplos idiomas

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

👨‍💻 Autor
Criado por Artenio Reis

🙏 Agradecimentos
Flask - Framework web

Scikit-learn - Machine Learning

NLTK - Processamento de Linguagem Natural

Python - Linguagem de programação

<div align="center">
⭐ Se este projeto foi útil, deixe uma estrela no GitHub!

Reportar Bug • Solicitar Feature

</div>
Python 3.8 ou superior

pip (gerenciador de pacotes Python)
