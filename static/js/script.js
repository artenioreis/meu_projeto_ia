// Elementos do DOM
const chatMessages = document.getElementById('chat-messages');
const inputPergunta = document.getElementById('input-pergunta');
const btnEnviar = document.getElementById('btn-enviar');
const btnLimpar = document.getElementById('btn-limpar');
const btnRecarregar = document.getElementById('btn-recargar');
const btnAdicionarFab = document.getElementById('btn-adicionar-fab');
const modalConhecimento = document.getElementById('modal-conhecimento');
const btnFecharModal = document.getElementById('btn-fechar-modal');
const btnCancelarModal = document.getElementById('btn-cancelar-modal');
const btnAdicionarConhecimento = document.getElementById('btn-adicionar-conhecimento');
const inputConhecimento = document.getElementById('input-conhecimento');

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    inputPergunta.focus();
});

// Enviar pergunta
btnEnviar.addEventListener('click', enviarPergunta);
inputPergunta.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        enviarPergunta();
    }
});

// Limpar chat
btnLimpar.addEventListener('click', function() {
    if (confirm('Tem certeza que deseja limpar o chat?')) {
        chatMessages.innerHTML = `
            <div class="message ai-message">
                <div class="message-avatar">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="message-content">
                    <div class="message-text">
                        Chat limpo! Estou pronto para novas perguntas. 🤖
                    </div>
                    <div class="message-time">Agora</div>
                </div>
            </div>
        `;
    }
});

// Recarregar IA
btnRecarregar.addEventListener('click', function() {
    btnRecarregar.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Recarregando...';
    btnRecarregar.disabled = true;
    
    fetch('/api/recarregar', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            alert(data.mensagem);
            btnRecarregar.innerHTML = '<i class="fas fa-sync-alt"></i> Recarregar IA';
            btnRecarregar.disabled = false;
        })
        .catch(error => {
            alert('Erro ao recarregar IA: ' + error);
            btnRecarregar.innerHTML = '<i class="fas fa-sync-alt"></i> Recarregar IA';
            btnRecarregar.disabled = false;
        });
});

// Modal de conhecimento
btnAdicionarFab.addEventListener('click', function() {
    modalConhecimento.classList.add('show');
    inputConhecimento.focus();
});

btnFecharModal.addEventListener('click', fecharModal);
btnCancelarModal.addEventListener('click', fecharModal);

btnAdicionarConhecimento.addEventListener('click', function() {
    const conhecimento = inputConhecimento.value.trim();
    
    if (!conhecimento) {
        alert('Por favor, digite algum conhecimento!');
        return;
    }
    
    btnAdicionarConhecimento.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Adicionando...';
    btnAdicionarConhecimento.disabled = true;
    
    fetch('/api/adicionar_conhecimento', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ conhecimento: conhecimento })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.mensagem);
        if (data.sucesso) {
            fecharModal();
            inputConhecimento.value = '';
            
            // Adiciona mensagem no chat
            adicionarMensagem('knowledge', `Conhecimento adicionado: "${conhecimento.substring(0, 50)}..."`);
        }
    })
    .catch(error => {
        alert('Erro ao adicionar conhecimento: ' + error);
    })
    .finally(() => {
        btnAdicionarConhecimento.innerHTML = '<i class="fas fa-save"></i> Adicionar Conhecimento';
        btnAdicionarConhecimento.disabled = false;
    });
});

function fecharModal() {
    modalConhecimento.classList.remove('show');
}

// Fechar modal clicando fora
modalConhecimento.addEventListener('click', function(e) {
    if (e.target === modalConhecimento) {
        fecharModal();
    }
});

// Função para enviar pergunta
function enviarPergunta() {
    const pergunta = inputPergunta.value.trim();
    
    if (!pergunta) {
        alert('Por favor, digite uma pergunta!');
        return;
    }
    
    // Adiciona mensagem do usuário
    adicionarMensagem('user', pergunta);
    
    // Limpa input
    inputPergunta.value = '';
    
    // Mostra indicador de digitação
    const typingIndicator = adicionarMensagem('ai', '...', true);
    
    // Envia para a API
    fetch('/api/perguntar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ pergunta: pergunta })
    })
    .then(response => response.json())
    .then(data => {
        // Remove indicador de digitação
        typingIndicator.remove();
        
        if (data.sucesso) {
            adicionarMensagem('ai', data.resposta);
        } else {
            adicionarMensagem('ai', '❌ ' + data.resposta);
        }
    })
    .catch(error => {
        typingIndicator.remove();
        adicionarMensagem('ai', '❌ Erro de conexão: ' + error);
    });
}

// Função para adicionar mensagem no chat
function adicionarMensagem(tipo, texto, isTyping = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${tipo === 'user' ? 'user-message' : 'ai-message'}`;
    
    const timestamp = new Date().toLocaleTimeString('pt-BR', { 
        hour: '2-digit', 
        minute: '2-digit' 
    });
    
    if (tipo === 'knowledge') {
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas fa-plus-circle"></i>
            </div>
            <div class="message-content" style="background: #fef3c7; border: 2px dashed #f59e0b;">
                <div class="message-text">
                    <i class="fas fa-info-circle" style="color: #f59e0b;"></i>
                    ${texto}
                </div>
                <div class="message-time">${timestamp}</div>
            </div>
        `;
    } else {
        messageDiv.innerHTML = `
            <div class="message-avatar">
                <i class="fas ${tipo === 'user' ? 'fa-user' : 'fa-robot'}"></i>
            </div>
            <div class="message-content">
                <div class="message-text">${texto}</div>
                <div class="message-time">${isTyping ? 'Digitando...' : timestamp}</div>
            </div>
        `;
    }
    
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    
    return messageDiv;
}