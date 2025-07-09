#!/bin/bash

# Script para executar o projeto completo de análise de projetos

echo "🚀 Iniciando setup do projeto de análise de projetos..."

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para imprimir mensagens coloridas
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    print_error "Python3 não está instalado. Instale Python3 primeiro."
    exit 1
fi

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    print_error "pip3 não está instalado. Instale pip3 primeiro."
    exit 1
fi

# Função para instalar dependências
install_dependencies() {
    local dir=$1
    print_status "Instalando dependências em $dir..."
    
    if [ -f "$dir/requirements.txt" ]; then
        cd "$dir"
        pip3 install -r requirements.txt
        cd ..
    else
        print_warning "requirements.txt não encontrado em $dir"
    fi
}

# Instalar dependências em todos os módulos
install_dependencies "ml_model"
install_dependencies "api"
install_dependencies "chatbot"

print_status "Dependências instaladas com sucesso!"

# Treinar o modelo
print_status "Treinando modelo de Machine Learning..."
cd ml_model
python3 model.py

if [ $? -eq 0 ]; then
    print_status "Modelo treinado com sucesso!"
else
    print_error "Erro no treinamento do modelo"
    exit 1
fi

cd ..

# Função para mostrar menu
show_menu() {
    echo ""
    echo "🎯 Projeto de Análise de Sucesso de Projetos"
    echo "=========================================="
    echo "1. Iniciar API"
    echo "2. Iniciar Chatbot"
    echo "3. Executar API em background e Chatbot"
    echo "4. Testar API"
    echo "5. Sair"
    echo ""
}

# Função para testar API
test_api() {
    print_status "Testando API..."
    
    # Verificar se a API está rodando
    if curl -s http://localhost:5000/health > /dev/null; then
        print_status "API está funcionando!"
        
        # Fazer teste de previsão
        print_status "Testando previsão..."
        curl -X POST http://localhost:5000/predict \
            -H "Content-Type: application/json" \
            -d '{
                "duracao": 8,
                "orcamento": 650000,
                "tamanho_equipe": 12,
                "recursos": "Alto"
            }' | python3 -m json.tool
    else
        print_error "API não está rodando. Inicie a API primeiro."
    fi
}

# Função para iniciar API
start_api() {
    print_status "Iniciando API..."
    cd api
    python3 app.py
    cd ..
}

# Função para iniciar chatbot
start_chatbot() {
    print_status "Iniciando Chatbot..."
    cd chatbot
    python3 chatbot.py
    cd ..
}

# Função para executar API em background e chatbot
start_both() {
    print_status "Iniciando API em background..."
    cd api
    python3 app.py &
    API_PID=$!
    cd ..
    
    print_status "Aguardando API inicializar..."
    sleep 3
    
    print_status "Iniciando Chatbot..."
    cd chatbot
    python3 chatbot.py
    cd ..
    
    # Finalizar API ao sair do chatbot
    print_status "Finalizando API..."
    kill $API_PID 2>/dev/null
}

# Loop principal
while true; do
    show_menu
    read -p "Escolha uma opção (1-5): " choice
    
    case $choice in
        1)
            start_api
            ;;
        2)
            start_chatbot
            ;;
        3)
            start_both
            ;;
        4)
            test_api
            ;;
        5)
            print_status "Saindo..."
            exit 0
            ;;
        *)
            print_error "Opção inválida. Escolha entre 1-5."
            ;;
    esac
done
