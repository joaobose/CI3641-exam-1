# Notas (1er Examen) 17-10490

**Nota total: 28 / 30**

## Pregunta 1

**Nota: 5 / 5**

El lenguaje escogido es **Javascript**

### Parte a

Me gusta mucho como agregas ejemplos para aclarar los conceptos que explicas.

El tema de los módulos en Node.js está super interesante. Qué extraño que no permita usar el manejo de módulos nativo del lenguaje y que tenga que proponer alternativas. Sería cool estudiar por qué tomaron esa decisión.

Excelente resumen de las características del lenguaje.

### Parte b

Buena implementación par ambas funciones. En particular, qué interesante forma de implementar el producto de matrices. Me gustó mucho esa forma de atacar el problema.

## Pregunta 2

**Nota: 5 / 5**

Usando variables:

* `X` = 4
* `Y` = 9
* `Z` = 0

### Parte a (alcance estático, asociación profunda)

Respuesta esperada:

```
5 25
5 15
5 5
5 50
```

La respuesta dada coincide.

### Parte b (alcance dinámico, asociación profunda)

Respuesta esperada:

```
5 25
5 15
5 5
5 9
```

La respuesta dada coincide.

### Parte c (alcance estático, asociación superficial)

Respuesta esperada:

```
5 25
5 15
5 5
5 50
```

La respuesta dada coincide.

### Parte d (alcance dinámico, asociación profunda)

Respuesta esperada:

```
5 25
5 15
5 5
5 9
```

La respuesta dada coincide.

## Pregunta 3

**Nota: 5 / 5**

La estructura del código está bien y hay buena documentación. La explicación incluida en el pdf principal de la entrega también ayudó mucho a entender la estructura de la solución.

Tu forma de reservar y liberar espacio es eficiente.

Buenas pruebas unitarias para tu programa y con buena cobertura.

## Pregunta 4

**Nota: 5 / 5**

### Parte a

La corrida en frío bien.

La implementación de `zipWith` bien.

### Parte b

La corrida en frío bien.

Buena descripción de lo que hace el iterador y descubriste la secuencia que está produciendo.

La implementación de `suspenso` bien.

## Pregunta 5

**Nota: 5 / 5**

### Parte a

Buena implementación.

### Parte b

Buena traducción.

### Parte c

La traducción respecto a lo mostrado en la parte b está correcta.

### Análisis de desempeño

Buen análisis de desempeño.

## Pregunta 6

**Nota: 3/5**

La estructura del código está bien y hay buena documentación.

No logré ejecutar tu programa. Al ejecutarlo con Python3 me da un error de compilación.

```
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/runpy.py", line 170, in _run_module_as_main
    "__main__", mod_spec)
  File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/Users/ricardo/Documents/Trabajo/USB/Docencia/Profesor/CI-3641/EM2021/Examenes/Examen 1/Entregas/Joao Pinto - 17-10490/CI3641-exam-1/pregunta-6/src/main.py", line 1, in <module>
    from .expression import ExpressionTree, postfixToExpressionTree, prefixToExpressionTree
  File "/Users/ricardo/Documents/Trabajo/USB/Docencia/Profesor/CI-3641/EM2021/Examenes/Examen 1/Entregas/Joao Pinto - 17-10490/CI3641-exam-1/pregunta-6/src/expression.py", line 25
    return f'{self.value}'
```

Aparentemente, habrá problemas con la impresión. Toma en cuenta las reglas de precedencia, pero no las de asociatividad.

Si realizamos

```
MOSTRAR PRE 1 1 1 - -
```

El resultado es

```
1 - 1 - 1
```

Cuando debería ser

```
1 - (1 - 1)
```

Buenas pruebas unitarias para tu programa.

## GOLF

**Bytes: 246**

**Lenguaje escogido: C++**

Como la implementación es una aproximación, no la puedo valer como parte de la competencia. Aún así, está muy bien.