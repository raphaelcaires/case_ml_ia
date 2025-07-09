# Modelo de Machine Learning para Previsão de Sucesso de Projetos

## Descrição

Este módulo implementa um modelo de Machine Learning usando Random Forest para prever o sucesso de projetos com base em dados históricos.

## Funcionalidades

- Treinamento do modelo com dados históricos
- Avaliação de performance com métricas completas
- Previsão de sucesso para novos projetos
- Salvamento e carregamento do modelo treinado

## Como usar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Treinar o modelo

```bash
python model.py
```

### 3. Usar o modelo em código

```python
from model import ProjectSuccessPredictor

# Inicializar e carregar modelo treinado
predictor = ProjectSuccessPredictor()
predictor.load_model("project_success_model.pkl")

# Fazer previsão
resultado = predictor.predict(
    duracao=8, 
    orcamento=650000, 
    tamanho_equipe=12, 
    recursos="Alto"
)

print(f"Probabilidade de sucesso: {resultado['probability_success']:.2%}")
```

## Estrutura dos Dados

### Entrada (Features)
- `Duracao_meses`: Duração do projeto em meses
- `Orcamento`: Orçamento total do projeto em R$
- `Tamanho_equipe`: Número de pessoas na equipe
- `Recursos_disponiveis`: Nível de recursos (Alto, Médio, Baixo)

### Saída (Target)
- `Sucesso`: 1 para sucesso, 0 para fracasso

## Métricas de Avaliação

O modelo é avaliado usando:
- Acurácia
- Precisão
- Recall
- F1-Score
- Relatório de classificação completo

## Arquivos

- `model.py`: Implementação principal do modelo
- `requirements.txt`: Dependências necessárias
- `project_success_model.pkl`: Modelo treinado (gerado após execução)
