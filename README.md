<p align="center">
<img alt="Author" src="https://img.shields.io/badge/author-KarinneCristina-blue.svg">
<img alt="License" src="https://img.shields.io/badge/license-MIT-blue">
<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/karinnecristina/Case_gamers_club">
<img alt="Python" src="https://img.shields.io/badge/python-3.9+-blue.svg">
<img alt="Contributions Welcome" src="https://img.shields.io/badge/contributions-welcome-blue.svg">
<img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103https://github.com/ellerbrock/open-source-badges/">
</p>

# Case Técnico - [Gamers Club](https://gamersclub.gg/)

<br></br>
**Desafio:** Criar um ambiente mínimo local para realizar a ingestão dos dados fornecidos.
- Ingestão das tabelas na camada raw
- Padronização das tabelas e colunas na camada bronze.
<br></br>

## 🎯 Fluxo do projeto

<p align="center">
  <img src="imagens/arquitetura.png" >
</p>

<br></br>

## 🎨 Layout

<p align="center">
  <img src="imagens/minio.png" >
</p>

<br></br>

## ⚙️ Passo a passo para reproduzir o projeto
#### Instalação do docker:
[Linux](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt) -
[Windows](https://docs.docker.com/desktop/windows/install/)
#### Instalação do poetry (windows / linux):
[poetry](https://python-poetry.org/docs/)

#### Configurando o ambiente:
```bash
# Faça download dos arquivos no link
$ git clone https://github.com/karinnecristina/Case_gamers_club
```

```bash
# Ative o ambiente virtual
$ poetry env use python3
```
```bash
# Instale as dependências
$ poetry install
```
```bash
# Configure o protocolo S3a para fazer a comunicação com o Minio
Faça o download dos protocolos S3a no link:
* https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar - arquivo jar
* https://mvnrepository.com/artifact/com.amazonaws - arquivo java-sdk

Mova os arquivos anterios para:
$ /Users/<usuario>/spark/jars
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

<br></br> 

## 🛠 Ferramentas e Tecnologias utilizadas

- [Python](https://www.python.org/) - Linguagem de programação
- [Poetry](https://python-poetry.org/) - Gerenciamento de ambientes virtuais
- [Postgres](https://www.postgresql.org/) – Banco de dados
- [Apache Airflow](https://airflow.apache.org/) – Automatizar o pipeline
- [Minio](https://min.io/) – Data Lake
- [Docker](https://www.docker.com/) – Executar toda aplicação
- [Git](https://git-scm.com/) – Versionamento dos códigos

<br></br>

### 💪 Como contribuir para o projeto
---

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`

<br></br>

### Autor (a)
---

Feito com ❤️ por Karinne Cristina 👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Karinne-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/karinnecristinapereira/)](https://www.linkedin.com/in/karinnecristinapereira/) 
[![Gmail Badge](https://img.shields.io/badge/-karinnecristinapereira@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:karinnecristinapereira@gmail.com)](mailto:karinnecristinapereira@gmail.com)

<br></br>

### 📝 Licença
---

Este projeto esta sobe a licença [MIT](./LICENSE).
