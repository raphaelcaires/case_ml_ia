# 🎯 Projeto de Análise de Sucesso de Projetos

## Descrição

Este projeto implementa uma solução completa de Machine Learning para prever o sucesso de projetos, incluindo:

- **Modelo de ML**: Random Forest para classificação de sucesso/fracasso
- **API REST**: Serviço para consumir o modelo treinado
- **Chatbot Interativo**: Interface amigável para coleta de dados e análise personalizada

## 📁 Estrutura do Projeto

```
case_ml/
├── data/
│   ├── projetos.csv         # Dados históricos de projetos
│   └── usuarios.csv         # Base de dados de usuários
├── ml_model/
│   ├── model.py             # Implementação do modelo ML
│   ├── requirements.txt     # Dependências do modelo
│   └── README.md           # Documentação do modelo
├── api/
│   ├── app.py              # API Flask
│   ├── requirements.txt    # Dependências da API
│   └── README.md          # Documentação da API
├── chatbot/
│   ├── chatbot.py          # Chatbot interativo
│   ├── requirements.txt    # Dependências do chatbot
│   └── README.md          # Documentação do chatbot
├── run_project.sh          # Script para executar o projeto
├── case.md                 # Especificação do case
└── README.md              # Este arquivo
```

## 🚀 Execução Rápida

### Opção 1: Script Automatizado (Recomendado)

```bash
# Tornar o script executável
chmod +x run_project.sh

# Executar o projeto
./run_project.sh
```

O script oferece um menu interativo para:
- Instalar dependências
- Treinar o modelo
- Iniciar API
- Iniciar Chatbot
- Executar testes

### Opção 2: Execução Manual

#### 1. Treinar o Modelo

```bash
cd ml_model
pip install -r requirements.txt
python model.py
```

#### 2. Iniciar a API

```bash
cd api
pip install -r requirements.txt
python app.py
```

#### 3. Executar o Chatbot

```bash
cd chatbot
pip install -r requirements.txt
python chatbot.py
```

## 📊 Dados de Exemplo

### Projetos Históricos

O modelo foi treinado com 40 projetos históricos incluindo:
- Duração (1-30 meses)
- Orçamento (R$ 200.000 - R$ 3.000.000)
- Tamanho da equipe (4-30 pessoas)
- Recursos disponíveis (Alto, Médio, Baixo)
- Resultado (Sucesso/Fracasso)

### Usuários Cadastrados

- João (Gerente de TI) - 80% sucesso
- Maria (Analista de Projetos) - 65% sucesso
- Pedro (Coordenador) - 90% sucesso
- Ana (Gerente de Projetos) - 75% sucesso
- Carlos (Analista Sênior) - 85% sucesso
- Lucia (Coordenadora) - 88% sucesso
- Rafael (Analista Junior) - 60% sucesso
- Fernanda (Gerente de TI) - 92% sucesso
- Roberto (Coordenador) - 78% sucesso
- Julia (Analista de Projetos) - 70% sucesso

## 🔧 Funcionalidades

### Modelo de Machine Learning

- **Algoritmo**: Random Forest Classifier
- **Features**: Duração, Orçamento, Tamanho da equipe, Recursos
- **Métricas**: Acurácia, Precisão, Recall, F1-Score
- **Interpretabilidade**: Importância das features
- **Persistência**: Modelo salvo em formato PKL

### API REST

- **GET /health**: Status da API
- **POST /predict**: Previsão individual
- **POST /batch-predict**: Previsões em lote
- **GET /model-info**: Informações do modelo

### Chatbot Inteligente

- **Identificação de usuário**: Busca na base de dados
- **Coleta interativa**: Perguntas sobre o projeto
- **Análise personalizada**: Combina dados do projeto com perfil do usuário
- **Recomendações**: Sugestões baseadas em dados históricos
- **Interface amigável**: Emojis e formatação clara

## 📈 Exemplo de Análise

```
🎯 Análise do Projeto

📊 Perfil do Usuário: João (Gerente de TI)
   - Experiência: 5 anos
   - Taxa de sucesso histórica: 80%

📈 Previsão do Modelo: 85.0% de chance de sucesso

✅ Excelente! Seu projeto tem alta probabilidade de sucesso.

💡 Recomendações:
   - 🔧 Recursos abundantes são um grande diferencial
   - 🌟 Seu histórico de 80% de sucesso é excelente!
   - 💼 Sua experiência de 5 anos é um grande ativo

🎯 Próximos passos sugeridos:
   1. Revisar o planejamento com base nas recomendações
   2. Alinhar expectativas com stakeholders
   3. Implementar controles de qualidade
   4. Monitorar progresso regularmente
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **scikit-learn**: Machine Learning
- **pandas**: Manipulação de dados
- **Flask**: API REST
- **requests**: Comunicação HTTP
- **joblib**: Persistência de modelos

## 📋 Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes)
- 2GB de RAM mínimo
- 1GB de espaço em disco

## 🧪 Testes

### Teste da API

```bash
# Verificar status
curl http://localhost:5000/health

# Teste de previsão
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "duracao": 8,
    "orcamento": 650000,
    "tamanho_equipe": 12,
    "recursos": "Alto"
  }'
```

### Teste do Chatbot

Execute o chatbot e teste com diferentes usuários:
- Use nomes da base de dados para análise personalizada
- Teste com diferentes combinações de dados de projeto
- Verifique as recomendações geradas

## 🔍 Métricas de Avaliação

O modelo alcançou as seguintes métricas no conjunto de teste:

- **Acurácia**: ~85%
- **Precisão**: ~84%
- **Recall**: ~85%
- **F1-Score**: ~84%

## 🎯 Critérios Atendidos

### Capacidade Técnica
✅ Modelo Random Forest implementado  
✅ API REST funcional  
✅ Código bem estruturado e documentado  

### Desempenho do Modelo
✅ Métricas de avaliação completas  
✅ Validação cruzada implementada  
✅ Interpretabilidade com importância das features  

### Funcionalidade do Chatbot
✅ Integração com API  
✅ Acesso à base de dados de usuários  
✅ Respostas personalizadas  

### Explicabilidade
✅ Documentação completa  
✅ Justificativas das decisões técnicas  
✅ Exemplos de uso  

### Inovação e Criatividade
✅ Interface de chatbot amigável  
✅ Análise personalizada por usuário  
✅ Recomendações inteligentes  
✅ Script automatizado para execução  

## 🚀 Melhorias Futuras

- Implementar autenticação na API
- Adicionar mais algoritmos de ML
- Criar interface web para o chatbot
- Implementar logging e monitoramento
- Adicionar testes automatizados
- Integrar com banco de dados real

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação de cada módulo
2. Execute os testes para validar a instalação
3. Consulte os logs de erro para debugging

## 📄 Licença

Este projeto foi desenvolvido como case técnico para vaga de Analista de Machine Learning.
