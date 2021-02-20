# Overview

En este modulo tenemos la respuestas de la pregunta de 6 del examen.

# Ejecucion

Desde la carpeta `pregunta-6` ejecuta:

```
python3 -m src.main
```

# Tests

## Install Coverage

```
sudo pip3 install coverage
```

## Correr tests

Para ejecutar los tests, debido a que python es python, es necesario hacerlo desde la carpeta padre de la carpeta `pregunta-6`

```
cd ..
coverage run -m unittest pregunta-6.tests.expression_test
```

## Coverage reports

Luego de ejecutar los tests, ejecuta:

```
coverage report
```
