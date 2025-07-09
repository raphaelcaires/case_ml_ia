# API de Previsão de Sucesso de Projetos

## Descrição

API REST desenvolvida em Flask para servir o modelo de Machine Learning que prediz o sucesso de projetos.

## Endpoints

### GET /health
Verifica se a API está funcionando e se o modelo está carregado.

**Resposta:**
```json
{
  "status": "healthy",
  "message": "API de Previsão de Sucesso de Projetos está funcionando",
  "model_loaded": true
}
```

### POST /predict
Faz previsão de sucesso para um único projeto.

**Entrada:**
```json
{
  "duracao": 8,
  "orcamento": 650000,
  "tamanho_equipe": 12,
  "recursos": "Alto"
}
```

**Resposta:**
```json
{
  "prediction": {
    "success": true,
    "probability_success": 0.85,
    "probability_failure": 0.15
  },
  "input_data": {
    "duracao": 8,
    "orcamento": 650000,
    "tamanho_equipe": 12,
    "recursos": "Alto"
  },
  "interpretation": {
    "success_percentage": "85.0%",
    "status": "Sucesso",
    "confidence": "Alta"
  }
}
```

### POST /batch-predict
Faz previsões para múltiplos projetos.

**Entrada:**
```json
{
  "projects": [
    {
      "duracao": 8,
      "orcamento": 650000,
      "tamanho_equipe": 12,
      "recursos": "Alto"
    },
    {
      "duracao": 15,
      "orcamento": 1200000,
      "tamanho_equipe": 18,
      "recursos": "Médio"
    }
  ]
}
```

### GET /model-info
Retorna informações sobre o modelo.

**Resposta:**
```json
{
  "model_type": "Random Forest Classifier",
  "features": [
    "Duração (meses)",
    "Orçamento (R$)",
    "Tamanho da equipe",
    "Recursos disponíveis"
  ],
  "target": "Sucesso do projeto (0/1)",
  "resources_options": ["Alto", "Médio", "Baixo"],
  "trained": true
}
```

## Como usar

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Treinar o modelo primeiro
```bash
cd ../ml_model
python model.py
```

### 3. Iniciar a API
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

## Exemplo de uso com curl

```bash
# Verificar status
curl http://localhost:5000/health

# Fazer previsão
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "duracao": 8,
    "orcamento": 650000,
    "tamanho_equipe": 12,
    "recursos": "Alto"
  }'

# Obter informações do modelo
curl http://localhost:5000/model-info
```

## Validações

- `duracao`: Deve ser um número positivo
- `orcamento`: Deve ser um número positivo
- `tamanho_equipe`: Deve ser um número inteiro positivo
- `recursos`: Deve ser "Alto", "Médio" ou "Baixo"

## Tratamento de Erros

A API retorna códigos de erro apropriados:
- 400: Dados inválidos ou campos obrigatórios faltando
- 500: Erro interno do servidor ou modelo não carregado
