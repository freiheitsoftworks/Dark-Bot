# Projeto Dark Bot - Automação de Dark Channel com IA

## Requisitos Funcionais

### RF01 - Listagem de Serviços

- **Descrição**: O sistema deve listar todos os serviços disponíveis para seleção.
- **Prioridade**: 8
- **Critério de Aceitação**:

  - A lista de serviços deve ser carregada corretamente.
  - O usuário deve conseguir selecionar um serviço da lista.

  ### RF02 - Criar Perfil

- **Descrição**: O sistema deve permitir a criação de perfil para registro de um perfil real de alguma plataforma/rede social.
- **Prioridade**: 9
- **Critério de Aceitação**:

  - O perfil deve ser único e ficar registrado no banco de dados
  - Deve poder ser consultado normalmente
  - O nome, plataforma e url são essenciais.

  ### RF03 - Listar Perfis

- **Descrição**: O sistema deve permitir a listagem de perfis registrados.
- **Prioridade**: 5
- **Critério de Aceitação**:

  - Os perfis devem ser listados baseado no id
  - Todos os dados do perfil devem aparecer
  - Deve ser possível navegar para uma página de edição do perfil ao clickar no botão editar.

  ### RF03 - Editar Perfil

- **Descrição**: O sistema deve permitir a edição e visualização de todos os dados do perfil selecionado.
- **Prioridade**: 5
- **Critério de Aceitação**:
  - Todos os dados do perfil devem aparecer
  - Todos os do perfil devem aparecer (menos os que fazem referência a outros modelos)
  - Deve ser possível navegar e visualizar o perfil em um outra página

## Casos de Uso

### UC01 - Seleção de Serviços

- **Ator**: Usuário
- **Pré-condição**: Estar na página inicial
- **Fluxo principal**:
  1. O usuário acessa a página inicial.
  2. O sistema exibe a lista de serviços disponíveis.
  3. O usuário seleciona um serviço.
  4. O sistema exibe os detalhes do serviço escolhido.
- **Pós-condição**: --------------------------------
- **Exceção**: Se o serviço não estiver disponível, o sistema exibe uma mensagem de erro.

### UC02 - Criar Perfil

- **Ator**: Usuário
- **Pré-condição**: Estar na página de criação de perfil
- **Fluxo principal**:
  1. O usuário acessa a página de criação de perfil.
  2. O usuário deve colocar os dados formulário e então submeter
  3. O usuário seleciona um serviço.
  4. O sistema exibe os detalhes do serviço escolhido.
- **Pós-condição**: --------------------------------
- **Exceção**:
  - Se o serviço não estiver disponível, o sistema exibe uma mensagem de erro.
  - Se já existe um perfil com o mesmo nome e mesma plataforma, deve ser avisado que o perfil já existe.

================================================================

## Guia de Desenvolvimento

### Passo a Passo Durante a Criação do Projeto

Usando Ubuntu com Python já instalado:

1. Se necessário, configure Python corretamente:

   ```bash
   sudo apt-get install python-is-python3
   ```

2. Crie e ative o ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate

   para o windows é necessário rodar: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   e depois: .\venv\Scripts\Activate.ps1

   para instalar as libs do requirements.txt -> pip install -r requirements.txt
   ```

   > Se houver problema na criação do ambiente, apague o diretório `venv` e tente novamente.

3. Instale as bibliotecas necessárias:

   ```bash
   pip install pymongo mongoengine flask-mongoengine requests selenium Flask
   ```

4. Gere o arquivo `requirements.txt`:

   ```bash
   pip freeze > requirements.txt
   ```

5. Inicie o repositório Git:

   ```bash
   git init
   git add .
   git commit -m "Primeiro commit: estrutura inicial do projeto Flask"
   git branch -M main
   ```

6. Resolva problemas de autenticação Git (caso tenha múltiplas contas configuradas):

   - Modifique as credenciais locais:
     ```bash
     git config user.name "freiheitsoftworks"
     git config user.email "freiheitsoftworks@gmail.com"
     git credential-cache exit
     ```
   - Crie uma chave SSH para autenticação:
     Siga o guia oficial: [Gerando uma nova chave SSH](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

   - Configure o repositório remoto para usar SSH:
     ```bash
     git remote set-url origin git@github.com:freiheitsoftworks/Dark-Bot.git
     ```

7. Envie o código para o GitHub:
   ```bash
   git push -u origin main
   ```

### Solução de Problemas

- **Interface Gráfica do Backend**:
  Para acessar o backend gráfico no Linux:

  ```bash
  xhost +
  sudo apt-get install python3-tk python3-dev
  ```

- **Permissão negada para `git add`**:
  Corrija a propriedade dos arquivos:

  ```bash
  sudo chown -R $USER:$USER .git
  ```

- **Permissão negada para o ambiente virtual (`venv`)**:
  Corrija a propriedade do diretório:
  ```bash
  sudo chown -R $USER:$USER ~/Área\ de\ Trabalho/Projetos\ Pessoais/dark-bot/venv
  ```

### Comando Especial

Para resetar containers Docker:

```bash
docker stop $(docker ps -aq) &&
docker rm $(docker ps -aq) &&
docker-compose down -v &&
docker volume prune -f
```

pip install flask[async] <- flask com await
