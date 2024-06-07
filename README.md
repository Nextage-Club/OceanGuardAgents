# Projeto de Planejamento e Resposta para Problemas de Saúde do Oceano

## Descrição do Projeto

Este projeto tem como objetivo planejar e gerar respostas abrangentes e factualmente precisas para problemas de saúde do oceano reportados por usuários. Utilizamos uma equipe de agentes configurados com o modelo Gemini Pro da Google para coletar informações, escrever respostas detalhadas e editar para garantir clareza e alinhamento com padrões organizacionais.

## Estrutura do Projeto

- **main.py**: Arquivo principal que configura os agentes, define as tarefas e gerencia a interação com o usuário.
- **utils.py**: Arquivo utilitário que contém funções auxiliares, como a obtenção da chave API do Google.
- **.env**: Arquivo de configuração para variáveis de ambiente, como chaves de API.

## Instruções de Uso

1. Clone o repositório para sua máquina local.
2. Instale as dependências listadas no arquivo `requirements.txt`.
3. Configure as variáveis de ambiente no arquivo `.env` (exemplo de conteúdo do `.env`):
    ```
    GOOGLE_API_KEY=your_google_api_key_here
    ```
4. Execute o arquivo `main.py` para iniciar a interação com o usuário.

### Passos Detalhados

1. **Obtenção da Localização e Problema**:
    - O usuário deve fornecer sua localização e uma descrição do problema de saúde do oceano.
2. **Geração de Resposta**:
    - Os agentes configurados irão coletar informações, escrever uma resposta detalhada e editar para garantir clareza e precisão.
3. **Feedback do Usuário**:
    - O usuário pode fornecer feedback sobre a resposta gerada.
4. **Iteração**:
    - O usuário tem a opção de gerar novas respostas ou encerrar o programa.
5. **Revisão de Feedbacks**:
    - Os desenvolvedores podem revisar e gerenciar feedbacks fornecidos pelos usuários.

## Requisitos

- Python 3.8+
- Biblioteca `crewai`
- Biblioteca `langchain_google_genai`
- Outros requisitos listados em `requirements.txt`

## Dependências

- `crewai`
- `langchain_google_genai`
- Outras dependências especificadas em `requirements.txt`

## Instalação

Execute o comando abaixo para instalar todas as dependências necessárias:

```
pip install -r requirements.txt
```

## Exemplo de Uso

```
python main.py
```

O programa solicitará a localização e o problema do usuário, gerará uma resposta e solicitará feedback. O usuário pode iterar através de novas gerações de respostas e fornecer feedback adicional até que decida encerrar o programa.