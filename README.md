# passo a passo de criação

usando ubuntu e python já instalado

Dia 1:

(usar pytgon-is-pthon3 se não estiver configurado corretamente)
python -m venv venv (apagar venv se bugar criação)
source venv/bin/activate (ativa ambiente)
instalando pymongo, requests, selenium, Flask
pip freeze > requirements.txt
iniciando repositorio:
git init
git add .
git commit -m "Primeiro commit: estrutura inicial do projeto Flask"
git branch -M main
problema com o push, pois as configs de autenticação (global) são para outra conta no github (usada localmente)

git config user.name freiheitsoftworks (alterando credenciais locamente)
git config user.email freiheitsoftworks@gmail.com
git credentials reject
input -> url=https://github.com/freiheitsoftworks/Dark-Bot.git
git credential-cache exit
git config --list (visualizar novas credenciais)

criando autenticação para a conta
https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
para usar CHAVE SSH no repositório ao fim das configurações:
git remote set-url origin git@github.com:freiheitsoftworks/Dark-Bot.git

git push -u origin main

para liberar backend acessar interface gráfica

> xhost +
> sudo apt-get install python3-tk python3-dev (linux não vem com o tkinter)

problema de permissão para git add -> sudo chown -R $USER:$USER .git

COMANDO ESPECIAL (resentando containeres):

docker stop $(docker ps -aq) &&
docker rm $(docker ps -aq) &&
docker-compose down -v &&
docker volume prune -f
