from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Adicionar o diretório do modelo ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ml_model'))

from model import ProjectSuccessPredictor

app = Flask(__name__)
CORS(app)

# Inicializar o preditor
predictor = ProjectSuccessPredictor()

# Carregar modelo treinado
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'ml_model', 'project_success_model.pkl')

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        'status': 'healthy',
        'message': 'API de Previsão de Sucesso de Projetos está funcionando',
        'model_loaded': predictor.is_trained
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint para fazer previsão de sucesso de projeto"""
    try:
        # Verificar se o modelo está carregado
        if not predictor.is_trained:
            if not predictor.load_model(MODEL_PATH):
                return jsonify({
                    'error': 'Modelo não pôde ser carregado',
                    'message': 'Certifique-se de que o modelo foi treinado primeiro'
                }), 500
        
        # Obter dados da requisição
        data = request.get_json()
        
        # Validar dados obrigatórios
        required_fields = ['duracao', 'orcamento', 'tamanho_equipe', 'recursos']
        missing_fields = [field for field in required_fields if field not in data]
        
        if missing_fields:
            return jsonify({
                'error': 'Campos obrigatórios faltando',
                'missing_fields': missing_fields
            }), 400
        
        # Validar valores
        duracao = data['duracao']
        orcamento = data['orcamento']
        tamanho_equipe = data['tamanho_equipe']
        recursos = data['recursos']
        
        if not isinstance(duracao, (int, float)) or duracao <= 0:
            return jsonify({'error': 'Duração deve ser um número positivo'}), 400
        
        if not isinstance(orcamento, (int, float)) or orcamento <= 0:
            return jsonify({'error': 'Orçamento deve ser um número positivo'}), 400
        
        if not isinstance(tamanho_equipe, int) or tamanho_equipe <= 0:
            return jsonify({'error': 'Tamanho da equipe deve ser um número inteiro positivo'}), 400
        
        if recursos not in ['Alto', 'Médio', 'Baixo']:
            return jsonify({'error': 'Recursos deve ser: Alto, Médio ou Baixo'}), 400
        
        # Fazer previsão
        prediction_result = predictor.predict(duracao, orcamento, tamanho_equipe, recursos)
        
        # Preparar resposta
        response = {
            'prediction': {
                'success': bool(prediction_result['prediction']),
                'probability_success': prediction_result['probability_success'],
                'probability_failure': prediction_result['probability_failure']
            },
            'input_data': {
                'duracao': duracao,
                'orcamento': orcamento,
                'tamanho_equipe': tamanho_equipe,
                'recursos': recursos
            },
            'interpretation': {
                'success_percentage': f"{prediction_result['probability_success'] * 100:.1f}%",
                'status': 'Sucesso' if prediction_result['prediction'] else 'Fracasso',
                'confidence': 'Alta' if max(prediction_result['probability_success'], prediction_result['probability_failure']) > 0.7 else 'Média' if max(prediction_result['probability_success'], prediction_result['probability_failure']) > 0.5 else 'Baixa'
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({
            'error': 'Erro interno do servidor',
            'message': str(e)
        }), 500

@app.route('/model-info', methods=['GET'])
def model_info():
    """Endpoint para obter informações sobre o modelo"""
    try:
        if not predictor.is_trained:
            if not predictor.load_model(MODEL_PATH):
                return jsonify({
                    'error': 'Modelo não pôde ser carregado'
                }), 500
        
        return jsonify({
            'model_type': 'Random Forest Classifier',
            'features': [
                'Duração (meses)',
                'Orçamento (R$)',
                'Tamanho da equipe',
                'Recursos disponíveis'
            ],
            'target': 'Sucesso do projeto (0/1)',
            'resources_options': ['Alto', 'Médio', 'Baixo'],
            'trained': predictor.is_trained
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Erro ao obter informações do modelo',
            'message': str(e)
        }), 500

@app.route('/batch-predict', methods=['POST'])
def batch_predict():
    """Endpoint para fazer previsões em lote"""
    try:
        if not predictor.is_trained:
            if not predictor.load_model(MODEL_PATH):
                return jsonify({
                    'error': 'Modelo não pôde ser carregado'
                }), 500
        
        data = request.get_json()
        
        if 'projects' not in data or not isinstance(data['projects'], list):
            return jsonify({
                'error': 'Formato inválido. Esperado: {"projects": [...]}'
            }), 400
        
        results = []
        for i, project in enumerate(data['projects']):
            try:
                prediction_result = predictor.predict(
                    project['duracao'],
                    project['orcamento'],
                    project['tamanho_equipe'],
                    project['recursos']
                )
                
                results.append({
                    'project_index': i,
                    'success': bool(prediction_result['prediction']),
                    'probability_success': prediction_result['probability_success'],
                    'success_percentage': f"{prediction_result['probability_success'] * 100:.1f}%"
                })
                
            except Exception as e:
                results.append({
                    'project_index': i,
                    'error': str(e)
                })
        
        return jsonify({
            'results': results,
            'total_projects': len(data['projects'])
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Erro no processamento em lote',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    print("Iniciando API de Previsão de Sucesso de Projetos...")
    print("Endpoints disponíveis:")
    print("  GET  /health - Verificar status da API")
    print("  POST /predict - Fazer previsão individual")
    print("  POST /batch-predict - Fazer previsões em lote")
    print("  GET  /model-info - Informações sobre o modelo")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
