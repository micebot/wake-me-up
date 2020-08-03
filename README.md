# WakeMeUp 🧀 [![pipeline status](https://gitlab.com/micebot/wake-me-up/badges/master/pipeline.svg)](https://gitlab.com/micebot/wake-me-up/-/commits/master)

Este projeto tem o objetivo de evitar que nosso servidor "durma" no Heroku, uma
vez que nenhuma requisição seja realizada dentro dos 30min:

> [**Free Dyno Hours**: *If an app has a free web dyno, and that dyno receives
>no web traffic in a 30-minute period, it will sleep. In addition to the web
dyno sleeping, the worker dyno (if present) will also
>sleep.*](https://devcenter.heroku.com/articles/free-dyno-hours)

Assim, para evitar que nossa aplicação seja interrompida, esse projeto faz com
que seja realizada uma requisição de `x` em `x` minutos para API permanecer
online.

## Executando

1. Clone e instale as dependências com o [poetry](https://python-poetry.org/docs/#installation):
```
git clone https://github.com/micebot/wake-me-up.git
cd ./wake-me-up

poetry install
poetry shell         # depois que .venv for criado.
```

2. Defina as variáveis de ambiente:

- `INTERVAL`: tempo em segundos de intervalo entre requisições. Exemplo:
considerando que você queira que seja realiza uma requisição a cada 15min,
utilize o valor `900`.
- `ENDPOINTS`: recurso a ser requisitado entre os intervalos. Será realizada uma
requisição GET para a URL especificada. Pode ser uma lista de recursos.

3. Execute:

```
py -m wakemeup
```