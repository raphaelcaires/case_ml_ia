# 🚀 Instruções de Uso - Projeto de Análise de Sucesso de Projetos

## ⚡ Execução Rápida

### 1. Demonstração Completa
```bash
# Executar demonstração completa do projeto
./demo_complete.sh
```

### 2. Execução Interativa
```bash
# Menu interativo para usar o projeto
./run_project.sh
```

### 3. Execução Manual por Componente

#### Treinar Modelo
```bash
cd ml_model
../venv/bin/python model.py
```

#### Iniciar API
```bash
cd api
../venv/bin/python app.py
```

#### Executar Chatbot
```bash
cd chatbot
../venv/bin/python chatbot.py
```

## 📊 Testando o Sistema

### 1. Teste da API via curl

```bash
# Verificar status
curl http://localhost:5000/health

# Previsão de sucesso
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "duracao": 8,
    "orcamento": 650000,
    "tamanho_equipe": 12,
    "recursos": "Alto"
  }'

# Previsão de risco
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "duracao": 20,
    "orcamento": 300000,
    "tamanho_equipe": 3,
    "recursos": "Baixo"
  }'
```

### 2. Teste do Chatbot

Execute o chatbot e teste com diferentes usuários:

**Usuários disponíveis na base:**
- João (Gerente de TI) - 80% sucesso
- Maria (Analista de Projetos) - 65% sucesso
- Pedro (Coordenador) - 90% sucesso
- Ana (Gerente de Projetos) - 75% sucesso
- Carlos (Analista Sênior) - 85% sucesso

**Cenários de teste:**
1. **Projeto de Alto Sucesso**: 6 meses, R$500.000, 10 pessoas, recursos Alto
2. **Projeto de Risco**: 18 meses, R$300.000, 5 pessoas, recursos Baixo
3. **Projeto Médio**: 10 meses, R$800.000, 13 pessoas, recursos Médio

## 🎯 Fluxo de Uso Completo

### 1. Preparação
```bash
# Clonar/baixar o projeto
# Navegar para o diretório do projeto
cd case_ml

# Tornar scripts executáveis
chmod +x *.sh
```

### 2. Primeira Execução
```bash
# Executar demonstração completa
./demo_complete.sh
```

### 3. Uso Interativo
```bash
# Executar menu interativo
./run_project.sh
```

### 4. Desenvolvimento/Teste
```bash
# Testar componentes individualmente
# Modificar dados em data/
# Retreinar modelo
# Testar API
# Ajustar chatbot
```

## 🔧 Personalização

### 1. Adicionar Novos Usuários
Edite `data/usuarios.csv`:
```csv
11,NovoUsuario,Cargo,Projetos,Anos,Sucesso%
```

### 2. Adicionar Novos Projetos
Edite `data/projetos.csv`:
```csv
41,duracao,orcamento,equipe,recursos,sucesso
```

### 3. Retreinar Modelo
```bash
cd ml_model
../venv/bin/python model.py
```

### 4. Modificar API
Edite `api/app.py` para adicionar novos endpoints ou funcionalidades.

### 5. Personalizar Chatbot
Edite `chatbot/chatbot.py` para modificar:
- Perguntas feitas ao usuário
- Análise de respostas
- Recomendações geradas

## 🐛 Resolução de Problemas

### Problema: Modelo não foi treinado
**Solução:**
```bash
cd ml_model
../venv/bin/python model.py
```

### Problema: API não responde
**Solução:**
```bash
# Verificar se está rodando
curl http://localhost:5000/health

# Se não estiver, iniciar
cd api
../venv/bin/python app.py
```

### Problema: Chatbot não encontra usuário
**Solução:**
- Verificar se o nome está na base `data/usuarios.csv`
- Usar nome exato (case-sensitive)
- Adicionar novo usuário se necessário

### Problema: Dependências não instaladas
**Solução:**
```bash
# Recriar ambiente virtual
python3 -m venv venv
source venv/bin/activate
pip install -r ml_model/requirements.txt
```

## 📈 Interpretação dos Resultados

### Probabilidade de Sucesso
- **> 80%**: Excelente chance de sucesso
- **60-80%**: Boa chance de sucesso
- **< 60%**: Chance baixa de sucesso

### Fatores Importantes
1. **Duração**: Projetos muito longos (>15 meses) têm menor chance de sucesso
2. **Orçamento**: Projetos com orçamento muito baixo (<R$400.000) são mais arriscados
3. **Equipe**: Equipes muito pequenas (<5) ou muito grandes (>20) podem ser problemáticas
4. **Recursos**: Recursos "Alto" aumentam significativamente as chances de sucesso

### Recomendações Típicas
- Ajustar orçamento para níveis adequados
- Balancear tamanho da equipe
- Dividir projetos longos em fases
- Garantir recursos adequados
- Considerar experiência do gerente

## 📊 Métricas do Modelo

O modelo Random Forest alcançou:
- **Acurácia**: ~85%
- **Precisão**: ~84%
- **Recall**: ~85%
- **F1-Score**: ~84%

## 🎯 Próximos Passos

1. **Produção**: Implementar em ambiente de produção
2. **Monitoramento**: Adicionar logs e métricas
3. **Segurança**: Implementar autenticação
4. **Escalabilidade**: Otimizar para maior volume
5. **Interface**: Criar interface web
6. **Integração**: Conectar com sistemas existentes

## 📞 Suporte

Para dúvidas técnicas:
1. Consulte a documentação de cada módulo
2. Execute os scripts de teste
3. Verifique logs de erro
4. Valide dados de entrada

---

**Desenvolvido como case técnico para vaga de Analista de Machine Learning**
