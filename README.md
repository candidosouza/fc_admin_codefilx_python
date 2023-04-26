# Admin Codeflix


> ## Repositório do curso Full Cycle 3.0

Microsserviço: Administração do Catálogo de vídeos com Python ( Back-end )

Com DDD e Clean Architecture

> ## Metodologias e Designs

* DDD
* Code Review
* PR Request Template
* Conventional Commits
* CI
* Observabilidade
* Repository Pattern
* Use Cases


> ## Bibliotecas e Ferramentas

* Autopep8
* Pylint
* pytest
* pytest-cov
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



Documentação em andamento...


(obs): documentar docker extra.host

> ## Instação

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
