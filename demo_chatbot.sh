#!/bin/bash

# Demo script para demonstrar o chatbot
echo "🤖 Demonstração do Chatbot de Análise de Projetos"
echo "=================================================="
echo ""
echo "Simulando entrada do usuário:"
echo "- Nome: João"
echo "- Duração: 8 meses"
echo "- Orçamento: 650000"
echo "- Equipe: 12 pessoas"
echo "- Recursos: Alto (opção 1)"
echo ""

cd /home/raphaelcaires/case_ml/chatbot

# Simular entrada do usuário
echo -e "João\n8\n650000\n12\n1\nn" | ../venv/bin/python chatbot.py
