import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib
import os

class ProjectSuccessPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.label_encoder = LabelEncoder()
        self.is_trained = False
        
    def load_data(self, filepath):
        """Carrega os dados de projetos do arquivo CSV"""
        try:
            data = pd.read_csv(filepath)
            return data
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return None
    
    def preprocess_data(self, data):
        """Prepara os dados para treinamento"""
        # Fazer uma cópia dos dados
        processed_data = data.copy()
        
        # Codificar variáveis categóricas
        processed_data['Recursos_disponiveis_encoded'] = self.label_encoder.fit_transform(processed_data['Recursos_disponiveis'])
        
        # Selecionar features
        features = ['Duracao_meses', 'Orcamento', 'Tamanho_equipe', 'Recursos_disponiveis_encoded']
        X = processed_data[features]
        y = processed_data['Sucesso']
        
        return X, y
    
    def train(self, data_path):
        """Treina o modelo com os dados fornecidos"""
        # Carregar dados
        data = self.load_data(data_path)
        if data is None:
            return False
        
        # Preprocessar dados
        X, y = self.preprocess_data(data)
        
        # Dividir dados em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Treinar modelo
        self.model.fit(X_train, y_train)
        
        # Fazer previsões
        y_pred = self.model.predict(X_test)
        
        # Calcular métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        print("=== Métricas do Modelo ===")
        print(f"Acurácia: {accuracy:.4f}")
        print(f"Precisão: {precision:.4f}")
        print(f"Recall: {recall:.4f}")
        print(f"F1-Score: {f1:.4f}")
        print("\n=== Relatório de Classificação ===")
        print(classification_report(y_test, y_pred))
        
        # Importância das features
        feature_importance = pd.DataFrame({
            'feature': ['Duracao_meses', 'Orcamento', 'Tamanho_equipe', 'Recursos_disponiveis'],
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\n=== Importância das Features ===")
        print(feature_importance)
        
        self.is_trained = True
        return True
    
    def predict(self, duracao, orcamento, tamanho_equipe, recursos):
        """Faz previsão para um novo projeto"""
        if not self.is_trained:
            raise ValueError("Modelo não foi treinado ainda!")
        
        # Codificar recursos
        recursos_encoded = self.label_encoder.transform([recursos])[0]
        
        # Preparar dados para previsão
        features = np.array([[duracao, orcamento, tamanho_equipe, recursos_encoded]])
        
        # Fazer previsão
        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0]
        
        return {
            'prediction': int(prediction),
            'probability_success': float(probability[1]),
            'probability_failure': float(probability[0])
        }
    
    def save_model(self, filepath):
        """Salva o modelo treinado"""
        if not self.is_trained:
            raise ValueError("Modelo não foi treinado ainda!")
        
        model_data = {
            'model': self.model,
            'label_encoder': self.label_encoder,
            'is_trained': self.is_trained
        }
        
        joblib.dump(model_data, filepath)
        print(f"Modelo salvo em: {filepath}")
    
    def load_model(self, filepath):
        """Carrega um modelo treinado"""
        try:
            model_data = joblib.load(filepath)
            self.model = model_data['model']
            self.label_encoder = model_data['label_encoder']
            self.is_trained = model_data['is_trained']
            print(f"Modelo carregado de: {filepath}")
            return True
        except Exception as e:
            print(f"Erro ao carregar modelo: {e}")
            return False

def main():
    # Inicializar o preditor
    predictor = ProjectSuccessPredictor()
    
    # Caminho dos dados
    data_path = "../data/projetos.csv"
    
    # Treinar o modelo
    print("Iniciando treinamento do modelo...")
    if predictor.train(data_path):
        print("Modelo treinado com sucesso!")
        
        # Salvar o modelo
        model_path = "project_success_model.pkl"
        predictor.save_model(model_path)
        
        # Teste de previsão
        print("\n=== Teste de Previsão ===")
        test_prediction = predictor.predict(
            duracao=8, 
            orcamento=650000, 
            tamanho_equipe=12, 
            recursos="Alto"
        )
        print(f"Previsão: {test_prediction}")
        
        success_prob = test_prediction['probability_success'] * 100
        print(f"Probabilidade de sucesso: {success_prob:.1f}%")
        
    else:
        print("Erro no treinamento do modelo!")

if __name__ == "__main__":
    main()
