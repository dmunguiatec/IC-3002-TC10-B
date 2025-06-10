# IC-3002 Tarea corta 10

Consideremos el problema 3SAT

**3SAT**.  
  **Entrada**. Una fórmula normal conjuntiva 3-CNF compuesta por $n$ variables booleanas $x_1,\dots,x_n$.  
  **Salida**. ${Si}$ cuando existe una asignación de valores de verdad a las variables tal que la evaluación de la fórmula completa sea verdadera, ${No}$ en cualquier otro caso.  

Una fórmula 3-CNF se compone por una secuencia de cláusulas, unidas por conjunciones. Cada cláusula contiene exactamente tres términos unidos por disjunciones. Cada término es una variable booleana $x_i$ o la negación de una variable booleana $\lnot x_i$.  

Por ejemplo, la siguiente es una fórmula 3CNF de tres cláusulas y cinco variables:
$$
(x_1 \lor \lnot x_2 \lor x_3​) \land (\lnot x_1 \lor x_4 \lor x_5​) \land (x_2 \lor \lnot x_3 \lor \lnot x_5​)
$$

Podemos representar esta fórmula en un archivo de texto en formato estándar `.cnf` de la siguiente manera:

```
p cnf 5 3
1 -2 3 0
-1 4 5 0
2 -3 -5 0
```

La primera línea inicia con `p` indicando que corresponde al preámbulo, luego el `cnf` indica que el archivo representa una fórmula normal conjuntiva de `5` variables y `3` cláusulas. Posteriormente el archivo contiene una línea para cada clásula, si el número es positivo representa a la variable correspondiente (`1` corresponde a $x_1$), y si es negativo representa la negación de la variable correspondiente (`-1` corresponde a $\lnot x_1$). El `0` al final de cada cláusula marca el fin de línea.

Así, la línea `-1 4 5 0` representa a la cláusula $(\lnot x_1 \lor x_4 \lor x_5)$.

Vamos a resolver este problema utilizando **minimización** por *simulated annealing*. Con este fin el archivo `simulated_annealing.py` implementa dicho algoritmo.

La clase de `dominio.Dominio3SAT` representa el dominio de soluciones al problema 3SAT. 

Debe implementar los métodos de la clase `dominio.Dominio3SAT`:
1. `generar()` y agregar un comentario que explique la estructura de datos que modela cada posible solución al problema.
2. `fcosto(sol)` y agregar un comentario que explique cómo se modela el costo de cada solución.
3. `vecino(sol)` y agregar un comentario que explique cuál es la heurística de optimización para generar vecinos que está utilizando y porqué decidió aplicarla (en lugar de cualquier otra posible).

No debe modificar código en `simulated_annealing.py` ni en los casos de prueba `simulated_annealing_test.py`.

## Cómo instalar el ambiente de desarrollo y ejecutar las pruebas localmente

Este proyecto requiere `python3`. Asegúrese que esté instalado en su distribución de linux.

Si no lo ha hecho anteriormente, crear un ambiente virtual para las dependencias

```bash
python3 -m venv .venv
```

Activar el ambiente virtual

```bash
source .venv/bin/activate
```

Instalar las dependencias

```bash
pip3 install -r requirements.txt
```

Ejecutar las pruebas

```bash
pytest -s -W ignore::DeprecationWarning
```

## Rúbrica

### Completitud (5 pts)

* (5 pts) La producción cumple totalmente con los requerimientos solicitados.
* (3 pts) La producción cumple parcialmente con los requerimientos solicitados.
* (1 pts) La producción, en su mayor parte, no cumple con los requerimientos solicitados.

### Correctitud (5 pts)

* (5 pts) El código pasa exitosamente todas las pruebas automatizadas.
* (3 pts) El código pasa la mayoría de las pruebas automatizadas.
* (1 pts) El código no pasa la mayoría de las pruebas automatizadas.

### Explicaciones (5 pts)

* (5 pts) El código incluye explicaciones concretas y consistentes con la implementación y con el problema para todos los métodos solicitados (`generar`, `fcosto` y `vecino`).
* (3 pts) El código incluye explicaciones concretas y consistentes con la implementación y con el problema para la mayoría de los métodos solicitados (`generar`, `fcosto` y `vecino`).
* (0 pts) El código no incluye explicaciones concretas y consistentes con la implementación y con el problema para la mayoría de los métodos solicitados (`generar`, `fcosto` y `vecino`).
