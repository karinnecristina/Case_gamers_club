## 🎯 Fluxo do projeto

<p align="center">
  <img src="imagens/arquitetura.png" >
</p>

## ⚙️ Passo a passo para reproduzir o projeto
#### Instalação do docker:
[Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt) -
[Windows](https://docs.docker.com/desktop/windows/install/)
#### Instalação do poetry (windows / linux):
[poetry](https://python-poetry.org/docs/)

#### Configurando o ambiente:
```bash
# Faça download dos arquivos no link
https://github.com/karinnecristina/Case_gamers_club
```

```bash
# Ative o ambiente virtual
$ poetry env use python3
```
```bash
# Instale as dependências
$ poetry install
```
#### Rodando a aplicação utilizando o airflow:

```bash
# Na pasta do projeto inicie o airflow
$ docker-compose up airflow-init
```
```bash
# Execute a aplicação
$ docker-compose up
```
#### Rodando a aplicação manualmente:

```bash
$ poetry run python pipeline.py
```