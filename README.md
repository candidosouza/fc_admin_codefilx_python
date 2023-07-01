# Projeto/Estudo em adamento..

# Documentação do Projeto - Microsserviço de Administração do Catálogo de Vídeos

## Visão Geral do Projeto
Este projeto consiste em um Microsserviço de Administração do Catálogo de Vídeos. Ele é responsável por gerenciar os conteúdos relacionados a vídeos, categorias, gêneros e membros do elenco. O microsserviço utiliza um banco de dados MySQL e oferece uma API REST para realizar operações de CRUD (Create, Read, Update, Delete).

O objetivo principal do projeto é criar um sistema administrativo que facilite a gestão dos vídeos, incluindo suas categorias, gêneros e membros do elenco. O desenvolvimento segue princípios de arquitetura limpa (Clean Architecture), Domain-Driven Design (DDD) e os princípios SOLID. Também são utilizados padrões de projeto para melhor organização e reutilização de código.

Além disso, o projeto inclui recursos como o upload de vídeos para um bucket específico, suportando dois tipos de vídeos: trailers e vídeos com conteúdo principal. Também é estabelecida uma comunicação utilizando o RabbitMQ para um serviço de codificação de vídeo, que transformará os vídeos no formato MPEG-DASH. O Kafka Connect é utilizado para o transporte de dados do banco de dados para outros microsserviços.

A linguagem de programação principal utilizada é o Python, em conjunto com os frameworks Django e Django REST Framework.

## Arquitetura do Projeto
A arquitetura do projeto segue os princípios de arquitetura limpa (Clean Architecture). A estrutura do projeto é organizada em camadas, visando a separação de responsabilidades e a facilidade de manutenção e testabilidade.

As principais camadas do projeto incluem:

1. **Camada de Aplicação**
2. **Camada de Domínio**
3. **Camada de Infraestrutura**

## Requisitos do Projeto
Os requisitos do projeto são definidos como:

1. **Gerenciamento de vídeos** : Possibilidade de criar, atualizar, visualizar e excluir vídeos do catálogo.
2. **Gerenciamento de categorias** : Capacidade de adicionar, atualizar, listar e remover categorias associadas aos vídeos.
3. **Gerenciamento de gêneros** : Funcionalidade para adicionar, atualizar, listar e remover gêneros associados aos vídeos.
4. **Gerenciamento de membros do elenco** : Recurso para adicionar, atualizar, listar e remover membros do elenco dos vídeos.
5. **Upload de vídeos** : Capacidade de fazer upload de vídeos (trailer e conteúdo principal) para um bucket específico.
6. **Serviço de codificação de vídeo** : Comunicação com um serviço externo de codificação de vídeo, que transformará os vídeos no formato MPEG-DASH.
7. **Transporte de dados com Kafka Connect** : Integração com o Kafka Connect para transportar dados do banco de dados para outros microsserviços.

## Design e Implementação
O projeto foi desenvolvido seguindo os princípios de DDD (Domain-Driven Design) e SOLID. Foram utilizados padrões de projeto para melhorar a estrutura e a reutilização de código.

Metodologias e Designs

* DDD
* Code Review
* PR Request Template
* Conventional Commits
* CI
* Observabilidade
* Repository Pattern
* Use Cases
* Mappers
* Dependency Injection

## Padrões de Projetos Utilizados
Os seguintes padrões de projeto foram aplicados no projeto:

* DTO (Data Transfer Object)
* Repository

## Bibliotecas e Ferramentas

* Autopep8
* Pylint
* pytest
* pytest-cov
* Dependency Injector
* Django
* DRF (Django Rest Framework)
* Git
* Github Actions
* Docker
* SonarCloud
* ELK Stack
* Prometheus
* Grafana
* OpenTelemetry


## Instação

Rodar o docker-compose
``` 
docker-compose up -d
```

> ## Testes

```
python -m unittest core.category.tests.unit.domain.test_unit_entities
```

```
python -m unittest core.__seedwork.tests.unit.domain.test_unit_repository
```

## coverage

```
pytest --ignore __pypackages__ --cov ./src
```
ou
```
pytest --ignore __pypackages__ --cov ./src --cov-report html:./__coverage
```
ou com pdm
```
pdm run test
```
```
pdm run test_cov 
```
```
pdm run test_cov_html 
```


### alinha todos os arquivos

```
autopep8 --in-place --recursive ./src
```

ou 

```
pdm run autopep8
```

## Manutenção e Suporte
Este projeto consiste apenas em estudo e NÃO possui manutenção e suporte.

## Contribuição
Este projeto consiste apenas em estudo e NÃO aceita contribuições.

## Licença
Este projeto consiste apenas em estudo e NÃO possui licença.

## Conclusão
O Microsserviço de Administração do Catálogo de Vídeos é uma solução robusta e flexível para gerenciar os vídeos, categorias, gêneros e membros do elenco de um catálogo. Com a utilização de padrões de projeto e boas práticas de desenvolvimento, o projeto oferece uma estrutura sólida e de fácil manutenção.

A arquitetura limpa, o DDD, o SOLID e os padrões de projeto aplicados garantem a separação de responsabilidades, a reutilização de código e a escalabilidade do sistema. Além disso, a integração com serviços externos, como o RabbitMQ e o Kafka Connect, proporciona uma comunicação eficiente e assíncrona entre os microsserviços.
