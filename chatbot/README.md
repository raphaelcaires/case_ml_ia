# Chatbot de Análise de Projetos

## Descrição

Chatbot interativo que coleta informações sobre projetos, acessa dados de usuários, e fornece previsões personalizadas sobre o sucesso de projetos usando o modelo de Machine Learning.

## Funcionalidades

- **Identificação do usuário**: Busca informações na base de dados de usuários
- **Coleta de dados**: Pergunta sobre duração, orçamento, equipe e recursos
- **Integração com API**: Faz chamadas para a API de previsão
- **Análise personalizada**: Combina dados do projeto com perfil do usuário
- **Recomendações**: Oferece sugestões baseadas nos dados coletados
- **Interface amigável**: Conversa natural com emojis e formatação clara

## Como usar

### 1. Pré-requisitos

Certifique-se de que:
- O modelo foi treinado (`ml_model/model.py`)
- A API está rodando (`api/app.py`)
- Os dados de usuários estão disponíveis (`data/usuarios.csv`)

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o chatbot

```bash
python chatbot.py
```

## Fluxo de Conversa

1. **Identificação**: O chatbot pergunta o nome do usuário
2. **Busca perfil**: Procura o usuário na base de dados
3. **Coleta dados**: Pergunta sobre o projeto:
   - Duração (meses)
   - Orçamento (R$)
   - Tamanho da equipe
   - Nível de recursos
4. **Análise**: Chama a API para fazer previsão
5. **Resposta personalizada**: Combina previsão com perfil do usuário
6. **Recomendações**: Oferece sugestões específicas

## Exemplo de Uso

```
🤖 Olá! Sou o assistente de análise de projetos.
Vou te ajudar a prever o sucesso do seu projeto com base em dados históricos.

Para começar, qual é o seu nome? João

✅ Usuário encontrado: João
Cargo: Gerente de TI
Experiência: 5 anos
Taxa de sucesso média: 80%

📋 Agora vou coletar informações sobre seu projeto:

Duração estimada do projeto (em meses): 8
Orçamento total do projeto (em R$): 650000
Número de pessoas na equipe: 12

Nível de recursos disponíveis:
1. Alto
2. Médio
3. Baixo
Escolha uma opção (1-3): 1

🔄 Processando análise...

🎯 **Análise do Projeto**

📊 **Perfil do Usuário:** João (Gerente de TI)
   - Experiência: 5 anos
   - Taxa de sucesso histórica: 80%

📈 **Previsão do Modelo:** 85.0% de chance de sucesso

✅ **Excelente!** Seu projeto tem alta probabilidade de sucesso.

💡 **Recomendações:**
   - 🔧 Recursos abundantes são um grande diferencial para o sucesso.
   - 🌟 Seu histórico de 80% de sucesso é excelente!
   - 💼 Sua experiência de 5 anos é um grande ativo.

🎯 **Próximos passos sugeridos:**
   1. Revisar o planejamento com base nas recomendações
   2. Alinhar expectativas com stakeholders
   3. Implementar controles de qualidade
   4. Monitorar progresso regularmente
```

## Recursos Personalizados

### Análise por Perfil de Usuário
- Combina dados históricos do usuário com previsão
- Considera experiência e taxa de sucesso anterior
- Oferece recomendações específicas por cargo

### Recomendações Inteligentes
- Analisa cada aspecto do projeto (duração, orçamento, equipe, recursos)
- Compara com padrões históricos de sucesso
- Sugere ajustes específicos

### Tratamento de Erros
- Valida entrada de dados
- Verifica disponibilidade da API
- Lida com usuários não encontrados na base

## Dependências

- `requests`: Para comunicação com API
- `pandas`: Para manipulação de dados de usuários
- `json`: Para processamento de respostas JSON

## Estrutura do Código

- `ProjectSuccessChatbot`: Classe principal do chatbot
- `load_users_data()`: Carrega base de dados de usuários
- `collect_project_data()`: Interface para coletar dados do projeto
- `get_prediction()`: Faz chamadas para API
- `generate_personalized_response()`: Gera análise personalizada
- `run_interactive_mode()`: Executa modo interativo

## Configuração

Por padrão, o chatbot espera:
- API rodando em `http://localhost:5000`
- Base de usuários em `../data/usuarios.csv`

Estes valores podem ser alterados no construtor da classe.
