import requests
import pandas as pd
import json
import sys
import os

class ProjectSuccessChatbot:
    def __init__(self, api_url="http://localhost:5000", users_data_path="../data/usuarios.csv"):
        self.api_url = api_url
        self.users_data_path = users_data_path
        self.current_user = None
        self.project_data = {}
        self.conversation_state = "start"
        
        # Carregar dados de usuários
        self.load_users_data()
        
    def load_users_data(self):
        """Carrega a base de dados de usuários"""
        try:
            self.users_df = pd.read_csv(self.users_data_path)
            print("Base de dados de usuários carregada com sucesso!")
        except Exception as e:
            print(f"Erro ao carregar base de usuários: {e}")
            self.users_df = pd.DataFrame()
    
    def get_user_by_name(self, name):
        """Busca usuário por nome"""
        if self.users_df.empty:
            return None
        
        user_row = self.users_df[self.users_df['Nome'].str.lower() == name.lower()]
        if not user_row.empty:
            return user_row.iloc[0].to_dict()
        return None
    
    def check_api_status(self):
        """Verifica se a API está funcionando"""
        try:
            response = requests.get(f"{self.api_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def get_prediction(self, duracao, orcamento, tamanho_equipe, recursos):
        """Faz chamada para a API de previsão"""
        try:
            data = {
                "duracao": duracao,
                "orcamento": orcamento,
                "tamanho_equipe": tamanho_equipe,
                "recursos": recursos
            }
            
            response = requests.post(f"{self.api_url}/predict", json=data, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            print(f"Erro ao fazer previsão: {e}")
            return None
    
    def generate_personalized_response(self, prediction_result):
        """Gera resposta personalizada baseada no usuário e previsão"""
        if not prediction_result:
            return "Desculpe, não foi possível fazer a previsão no momento. Tente novamente mais tarde."
        
        success_prob = prediction_result['prediction']['probability_success']
        success_percentage = prediction_result['interpretation']['success_percentage']
        
        # Resposta base
        response = f"🎯 **Análise do Projeto**\n\n"
        
        # Informações do usuário
        if self.current_user:
            user_success = self.current_user['Sucesso_medio']
            user_exp = self.current_user['Experiencia_anos']
            user_cargo = self.current_user['Cargo']
            
            response += f"📊 **Perfil do Usuário:** {self.current_user['Nome']} ({user_cargo})\n"
            response += f"   - Experiência: {user_exp} anos\n"
            response += f"   - Taxa de sucesso histórica: {user_success}%\n\n"
        
        # Resultado da previsão
        response += f"📈 **Previsão do Modelo:** {success_percentage} de chance de sucesso\n\n"
        
        # Análise personalizada
        if success_prob >= 0.8:
            response += "✅ **Excelente!** Seu projeto tem alta probabilidade de sucesso.\n"
        elif success_prob >= 0.6:
            response += "⚠️ **Boa chance!** Seu projeto tem probabilidade moderada de sucesso.\n"
        else:
            response += "🔴 **Atenção!** Seu projeto tem baixa probabilidade de sucesso.\n"
        
        # Recomendações baseadas nos dados
        response += "\n💡 **Recomendações:**\n"
        
        duracao = self.project_data['duracao']
        orcamento = self.project_data['orcamento']
        tamanho_equipe = self.project_data['tamanho_equipe']
        recursos = self.project_data['recursos']
        
        # Análise de duração
        if duracao > 12:
            response += f"   - ⏰ Duração de {duracao} meses é longa. Considere dividir em fases menores.\n"
        elif duracao < 3:
            response += f"   - ⏰ Duração de {duracao} meses pode ser muito curta para projetos complexos.\n"
        
        # Análise de orçamento
        if orcamento < 400000:
            response += f"   - 💰 Orçamento de R${orcamento:,} está abaixo da média. Considere aumentar o investimento.\n"
        elif orcamento > 1500000:
            response += f"   - 💰 Orçamento alto de R${orcamento:,}. Certifique-se de que há ROI adequado.\n"
        
        # Análise de equipe
        if tamanho_equipe < 5:
            response += f"   - 👥 Equipe pequena ({tamanho_equipe} pessoas). Considere reforçar com mais membros.\n"
        elif tamanho_equipe > 20:
            response += f"   - 👥 Equipe grande ({tamanho_equipe} pessoas). Atenção à coordenação e comunicação.\n"
        
        # Análise de recursos
        if recursos == "Baixo":
            response += "   - 🔧 Recursos limitados podem impactar o sucesso. Considere aumentar o suporte.\n"
        elif recursos == "Alto":
            response += "   - 🔧 Recursos abundantes são um grande diferencial para o sucesso.\n"
        
        # Recomendações baseadas no perfil do usuário
        if self.current_user:
            if self.current_user['Sucesso_medio'] > 80:
                response += f"   - 🌟 Seu histórico de {self.current_user['Sucesso_medio']}% de sucesso é excelente!\n"
            elif self.current_user['Sucesso_medio'] < 70:
                response += f"   - 📚 Considere buscar mentoria ou treinamento para melhorar sua taxa de sucesso.\n"
            
            if self.current_user['Experiencia_anos'] >= 5:
                response += f"   - 💼 Sua experiência de {self.current_user['Experiencia_anos']} anos é um grande ativo.\n"
        
        response += "\n🎯 **Próximos passos sugeridos:**\n"
        response += "   1. Revisar o planejamento com base nas recomendações\n"
        response += "   2. Alinhar expectativas com stakeholders\n"
        response += "   3. Implementar controles de qualidade\n"
        response += "   4. Monitorar progresso regularmente\n"
        
        return response
    
    def start_conversation(self):
        """Inicia a conversa com o usuário"""
        print("🤖 Olá! Sou o assistente de análise de projetos.")
        print("Vou te ajudar a prever o sucesso do seu projeto com base em dados históricos.\n")
        
        # Verificar API
        if not self.check_api_status():
            print("⚠️ Aviso: A API de previsão não está disponível. Certifique-se de que ela está rodando.")
            return
        
        # Identificar usuário
        user_name = input("Para começar, qual é o seu nome? ")
        self.current_user = self.get_user_by_name(user_name)
        
        if self.current_user:
            print(f"\n✅ Usuário encontrado: {self.current_user['Nome']}")
            print(f"Cargo: {self.current_user['Cargo']}")
            print(f"Experiência: {self.current_user['Experiencia_anos']} anos")
            print(f"Taxa de sucesso média: {self.current_user['Sucesso_medio']}%\n")
        else:
            print(f"\n⚠️ Usuário '{user_name}' não encontrado na base de dados.")
            print("Continuando sem dados históricos do usuário...\n")
        
        # Coletar dados do projeto
        self.collect_project_data()
        
        # Fazer previsão
        self.make_prediction()
    
    def collect_project_data(self):
        """Coleta dados do projeto do usuário"""
        print("📋 Agora vou coletar informações sobre seu projeto:\n")
        
        # Duração
        while True:
            try:
                duracao = float(input("Duração estimada do projeto (em meses): "))
                if duracao > 0:
                    self.project_data['duracao'] = duracao
                    break
                else:
                    print("❌ A duração deve ser um número positivo.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")
        
        # Orçamento
        while True:
            try:
                orcamento = float(input("Orçamento total do projeto (em R$): "))
                if orcamento > 0:
                    self.project_data['orcamento'] = orcamento
                    break
                else:
                    print("❌ O orçamento deve ser um número positivo.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")
        
        # Tamanho da equipe
        while True:
            try:
                tamanho_equipe = int(input("Número de pessoas na equipe: "))
                if tamanho_equipe > 0:
                    self.project_data['tamanho_equipe'] = tamanho_equipe
                    break
                else:
                    print("❌ O tamanho da equipe deve ser um número inteiro positivo.")
            except ValueError:
                print("❌ Por favor, digite um número inteiro válido.")
        
        # Recursos disponíveis
        while True:
            print("\nNível de recursos disponíveis:")
            print("1. Alto")
            print("2. Médio")
            print("3. Baixo")
            
            try:
                opcao = int(input("Escolha uma opção (1-3): "))
                if opcao == 1:
                    self.project_data['recursos'] = "Alto"
                    break
                elif opcao == 2:
                    self.project_data['recursos'] = "Médio"
                    break
                elif opcao == 3:
                    self.project_data['recursos'] = "Baixo"
                    break
                else:
                    print("❌ Opção inválida. Escolha 1, 2 ou 3.")
            except ValueError:
                print("❌ Por favor, digite um número válido.")
        
        print("\n✅ Dados coletados com sucesso!")
        print(f"Projeto: {self.project_data['duracao']} meses, R${self.project_data['orcamento']:,}, {self.project_data['tamanho_equipe']} pessoas, recursos {self.project_data['recursos']}")
    
    def make_prediction(self):
        """Faz a previsão e exibe resultado"""
        print("\n🔄 Processando análise...")
        
        prediction_result = self.get_prediction(
            self.project_data['duracao'],
            self.project_data['orcamento'],
            self.project_data['tamanho_equipe'],
            self.project_data['recursos']
        )
        
        if prediction_result:
            response = self.generate_personalized_response(prediction_result)
            print(f"\n{response}")
        else:
            print("\n❌ Erro ao fazer previsão. Verifique se a API está funcionando.")
        
        # Opção de fazer nova análise
        print("\n" + "="*50)
        nova_analise = input("Deseja analisar outro projeto? (s/n): ")
        if nova_analise.lower() in ['s', 'sim', 'y', 'yes']:
            self.project_data = {}
            self.collect_project_data()
            self.make_prediction()
    
    def run_interactive_mode(self):
        """Executa o modo interativo do chatbot"""
        try:
            self.start_conversation()
        except KeyboardInterrupt:
            print("\n\n👋 Obrigado por usar o assistente de análise de projetos!")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")

def main():
    print("🚀 Iniciando Chatbot de Análise de Projetos...")
    
    # Verificar se os arquivos necessários existem
    if not os.path.exists("../data/usuarios.csv"):
        print("❌ Arquivo de usuários não encontrado. Certifique-se de que ../data/usuarios.csv existe.")
        return
    
    # Inicializar e executar chatbot
    chatbot = ProjectSuccessChatbot()
    chatbot.run_interactive_mode()

if __name__ == "__main__":
    main()
