#!/bin/bash

# Script de demonstração completa do projeto
echo "🎯 PROJETO DE ANÁLISE DE SUCESSO DE PROJETOS"
echo "=============================================="
echo ""
echo "📋 Resumo do Projeto:"
echo "- Modelo de ML: Random Forest para prever sucesso de projetos"
echo "- API REST: Flask para servir o modelo"
echo "- Chatbot: Interface interativa para análise personalizada"
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_step() {
    echo -e "${BLUE}[PASSO $1]${NC} $2"
}

print_success() {
    echo -e "${GREEN}[SUCESSO]${NC} $1"
}

print_info() {
    echo -e "${YELLOW}[INFO]${NC} $1"
}

# Verificar se o modelo foi treinado
print_step "1" "Verificando se o modelo foi treinado..."
if [ -f "ml_model/project_success_model.pkl" ]; then
    print_success "Modelo treinado encontrado!"
else
    print_info "Treinando o modelo..."
    cd ml_model
    ../venv/bin/python model.py
    cd ..
    print_success "Modelo treinado com sucesso!"
fi

echo ""

# Verificar se a API está rodando
print_step "2" "Verificando se a API está rodando..."
if curl -s http://localhost:5000/health > /dev/null 2>&1; then
    print_success "API está rodando!"
else
    print_info "API não está rodando. Iniciando..."
    cd api
    ../venv/bin/python app.py &
    API_PID=$!
    cd ..
    sleep 3
    print_success "API iniciada!"
fi

echo ""

# Demonstração da API
print_step "3" "Demonstração da API"
echo "====================" 

echo ""
print_info "Testando endpoint /health:"
curl -s http://localhost:5000/health | python3 -m json.tool

echo ""
print_info "Testando previsão para projeto de sucesso:"
curl -s -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "duracao": 8,
    "orcamento": 650000,
    "tamanho_equipe": 12,
    "recursos": "Alto"
  }' | python3 -m json.tool

echo ""
print_info "Testando previsão para projeto de risco:"
curl -s -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "duracao": 20,
    "orcamento": 300000,
    "tamanho_equipe": 3,
    "recursos": "Baixo"
  }' | python3 -m json.tool

echo ""

# Demonstração do chatbot
print_step "4" "Demonstração do Chatbot"
echo "========================="

echo ""
print_info "Simulando conversa com o chatbot:"
echo "- Usuário: João (Gerente de TI)"
echo "- Projeto: 8 meses, R$650.000, 12 pessoas, recursos Alto"
echo ""

# Executar chatbot com entrada simulada
echo -e "João\n8\n650000\n12\n1\nn" | venv/bin/python chatbot/chatbot.py

echo ""

# Mostrar estrutura do projeto
print_step "5" "Estrutura do Projeto"
echo "===================="
echo ""
tree -I 'venv|__pycache__' . || ls -la

echo ""

# Mostrar métricas finais
print_step "6" "Métricas e Resultados"
echo "====================="
echo ""
print_info "Funcionalidades implementadas:"
echo "✅ Modelo Random Forest treinado com dados históricos"
echo "✅ API REST com endpoints para previsão"
echo "✅ Chatbot interativo com análise personalizada"
echo "✅ Integração com base de dados de usuários"
echo "✅ Recomendações baseadas em padrões históricos"
echo "✅ Documentação completa para cada componente"

echo ""
print_info "Arquivos principais:"
echo "- ml_model/model.py: Implementação do modelo ML"
echo "- api/app.py: API REST em Flask"
echo "- chatbot/chatbot.py: Chatbot interativo"
echo "- data/: Dados de exemplo (projetos e usuários)"
echo "- README.md: Documentação completa"

echo ""
print_success "Projeto concluído com sucesso!"
print_info "Para usar interativamente, execute: ./run_project.sh"

# Finalizar API se foi iniciada neste script
if [ ! -z "$API_PID" ]; then
    print_info "Finalizando API..."
    kill $API_PID 2>/dev/null
fi

echo ""
echo "🚀 Obrigado por testar o projeto!"
