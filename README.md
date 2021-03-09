# Tkey-Geek
Projeto teste.

Me baseei no site de número [#1 LIV Watches](https://unbounce.com/conversion-rate-optimization/ecommerce-landing-page-examples-sales/).

Para poder falar do produto [Tkey Magnetico](https://pt.aliexpress.com/item/4000720138527.html).

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com Python 3.8.3
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:Baihanu/tkey-geek.git tkey-geek
cd tkey-geek
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku.
2. Envie as configurações para o Heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o Heroku.

```console
heroku crete minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py´
heroku config:set DEBUG=False
# Configure o email
git push heroku master --force
```

[![Build Status](https://travis-ci.com/Baihanu/tkey-geek.svg?branch=main)](https://travis-ci.com/Baihanu/tkey-geek)
[![codecov](https://codecov.io/gh/Baihanu/tkey-geek/branch/main/graph/badge.svg?token=L0HG5FUI2C)](https://codecov.io/gh/Baihanu/tkey-geek)
