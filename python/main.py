# Warning Control
import warnings
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from utils import get_google_api_key

warnings.filterwarnings("ignore") # Ignora avisos que podem ser gerados durante a execução do código

# Configura o modelo Gemini Pro como LLM (Modelo de Linguagem)
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=get_google_api_key()) # Obtém a chave API do Google a partir de uma função utilitária

# Definição dos agentes
planner = Agent(
    role="Planejador de Conteúdo de Saúde do Oceano", # Cargo
    goal="Planejar conteúdo envolvente e factualmente preciso sobre problemas de saúde do oceano reportados pelos usuários em {location}", # Objetivo
    backstory="Você está trabalhando no planejamento de uma resposta abrangente aos problemas de saúde do oceano reportados pelos usuários em {location}. Você coleta informações sobre soluções para {problem}, passos que o usuário pode tomar, últimas notícias e eventos futuros relacionados ao problema em {location}.", # Contexto
    allow_delegation=False, # Define se um agente pode ou não comandar outros
    verbose=False, # Descreve o output do agente
    llm=llm # Associa o modelo de linguagem configurado anteriormente ao agente
)

writer = Agent(
    role="Redator de Conteúdo de Saúde do Oceano",
    goal="Escrever respostas perspicazes e factualmente precisas sobre problemas de saúde do oceano em {location}",
    backstory="Você está escrevendo uma resposta detalhada aos problemas de saúde do oceano reportados pelos usuários em {location}. Você baseia sua escrita nas informações fornecidas pelo Planejador de Conteúdo, garantindo oferecer soluções práticas para {problem}, passos a serem tomados, últimas notícias e eventos futuros relacionados ao problema em {location}.",
    allow_delegation=False,
    verbose=False,
    llm=llm
)

editor = Agent(
    role="Editor de Conteúdo de Saúde do Oceano",
    goal="Editar a resposta para alinhar com os padrões da organização e garantir clareza",
    backstory="Você é um editor que revisa a resposta escrita pelo Redator de Conteúdo. Seu objetivo é garantir que a resposta esteja clara, siga as melhores práticas jornalísticas, forneça pontos de vista equilibrados e evite grandes controvérsias quando possível.",
    allow_delegation=False,
    verbose=True,
    llm=llm
)

# Definição das tarefas
plan = Task(
    description=( # Descrição da tarefa
        "1. Priorizar as últimas tendências, principais atores e notícias relevantes sobre o problema de saúde do oceano {problem} em {location}.\n"
        "2. Identificar o público-alvo, considerando seus interesses e preocupações.\n"
        "3. Desenvolver um esboço detalhado do conteúdo, incluindo soluções para o problema reportado {problem}, passos que o usuário pode tomar, últimas notícias e eventos futuros em {location}.\n"
        "4. Incluir dados relevantes, fontes e garantir precisão factual."
    ),
    expected_output="Um plano de conteúdo abrangente com um esboço, análise do público e recursos.", # Output esperado
    agent=planner # Define qual agente vai executar a tarefa
)

write = Task(
    description=(
        "1. Usar o plano de conteúdo para elaborar uma resposta abrangente ao problema de saúde do oceano {problem} em {location}.\n"
        "2. Incluir soluções práticas e um guia passo a passo para o usuário.\n"
        "3. Buscar e fornecer as últimas notícias relacionadas ao problema de saúde do oceano {problem} e a localização {location} em fontes confiáveis na web.\n"
        "4. Listar eventos futuros relacionados à saúde do oceano em {location}.\n"
        "5. Incluir recursos e fontes relevantes para o problema e a localização mencionados.\n"
        "6. Garantir que a resposta esteja estruturada de maneira clara e envolvente.\n"
        "7. Revisar para corrigir erros gramaticais e alinhar com o tom da marca."
    ),
    expected_output="Uma resposta bem escrita em formato markdown, pronta para publicação, abordando apenas o problema descrito pelo usuário.",
    agent=writer
)

edit = Task(
    description=("Revisar a resposta para corrigir erros gramaticais e alinhar com o tom da marca."),
    expected_output="Uma resposta bem escrita em formato markdown, pronta para publicação, abordando apenas o problema descrito pelo usuário.",
    agent=editor
)

# Define a equipe de agentes
crew = Crew(
    agents=[planner, writer, editor], # Agentes
    tasks=[plan, write, edit], # Tarefas
)

# Listas para guardar as localizações e problemas
locations = []
problems = []

# Função que gera o resultado
def generate_result(locations, problems):
    location = input("Digite a sua localização: ") # Obtém a localização
    problem = input("Descrição do problema a ser reportado: ") # Obtém o problema
    locations.append(location) # Adiciona a localização à lista
    problems.append(problem) # Adiciona o problema à lista
    print("")
    print("Gerando resposta...")
    result = crew.kickoff(inputs={"location": location, "problem": problem}) # Gera o resultado
    return result

# Função que obtém o feedback
def get_feedback(feedbacks):
    feedback = input("Escreva aqui o feedback da resposta: ")
    feedbacks.append(feedback)

# Lista para guardar os feedbacks
feedbacks = []

generate_result(locations, problems)
print("")
get_feedback(feedbacks)

new_result = ""
while new_result != "NÃO": # Enquanto o usuário quiser gerar novas respostas
    new_result = input("Deseja gerar uma nova resposta? (Sim / Não): ").upper()
    if new_result == "SIM":
        print("")
        generate_result(locations, problems) # Gera nova resposta
        print("")
        get_feedback(feedbacks) # Obtém novo feedback
    elif new_result == "NÃO":
        print("")
        print("Obrigado por utilizar a nossa plataforma!")
    else:
        print("Entrada inválida. Digite Sim ou Não.")
        new_result = input("Deseja gerar uma nova resposta? (Sim / Não): ").upper()

print("")
print("----- Dev -----") # Área de desenvolvedor
read_feedbacks = input("Deseja ler os feedbacks? (Sim / Não): ").upper()

# Função que exibe os feedbacks e reports
def show_feedbacks(feedbacks, locations, problems):
    reports = locations + problems
    cont = 1
    cont2 = 1
    print("")
    print("----- Lista de Reports -----")
    for i in reports: # Exibe os reports
        print(f"{cont}. {i}")
        print("")
        cont += 1
    print("")
    print("----- Lista de Feedbacks -----") 
    for i in feedbacks: # Exibe os feedbacks
        print(f"{cont2}. {i}")
        print("")
        cont2 += 1

def end_program(): # Mensagem de finalização do programa
    print("")
    print("Programa Finalizado.")

if read_feedbacks == "SIM": # Se o dev quiser ver os feedbacks
    show_feedbacks(feedbacks, locations, problems)
    del_feedback = input("Deseja apagar algum feedback? (Sim / Não): ").upper()
    if del_feedback == "SIM": # Se o dev quiser apagar algum feedback
        element = int(input("Digite o número do feedback a ser apagado: "))
        element -= 1
        feedbacks.pop(element)
        show_feedbacks(feedbacks, locations, problems) # Mostra as listas, com o feedback apagado
        end_program()
    else:
        end_program()
else:
    end_program()