
# Complejidad Algoritmica

## Trabajo Parcial

### Integrantes

##### Daniel Jimenez
##### Diego Alosilla
##### Marco de la Cruz

# Introducción

El problema del agente viajero (tsp) es uno de los más estudiados en el campo de la optimización, ya que cuenta con diversas aplicaciones en la industria. Hace referencia a la visita   lugares o nodos (para entregar o recoger mercancías) con el fin resolver problemas que impidan minimizar algún objetivo (tiempo o costos) o maximizar algún otro.
La primera solución reportada para resolver el problema del Agente Viajero fue en 1954, cuando George Dantzig, Ray Fulkerson, y Selmer Johnson  publicaron la descripción de un método de solución del PAV (Problema del Agente Viaje o sus siglas en inglés TSP – Travel Sailsman Problem) titulado “Solutions of a large scale traveling salesman problem“ (Soluciones de gran escala para el problema del agente viajero) para resolver una instancia de 49 ciudades donde un agente viajero desea visitar un conjunto de ciudades, asignándoles un costo por visitar ciudades contiguas (distancia de traslado entre dos ciudades). Para esta solución se propusieron 2 condiciones: regresar a      la misma ciudad de la cual partió y no repetir ciudades con el objetivo de encontrar una ruta o un camino con el menor costo posible.


## Motivación

Resolver el problema del agente viajero(TSP) ya que es uno de los más estudiados en el campo de la optimización, lo tomamos como un reto, de esta forma nos motiva a investigar sobre los algoritmos más convenientes para este problema.

## Objetivos

●	Implementar un algoritmo el cual resuelva de manera eficiente el problema de las conexiones de los centros poblados en el país.

●	Analizar la conveniencia de usar las técnicas de "UDFS", "MST", "BellmanFord", "Jhonson", "Floyd-Warshall"

●	Analizar la complejidad del algoritmo que se implementará.


# Marco Teórico

Para la implementación del trabajo hemos utilizado el lenguaje de programación con los siguientes algoritmos:

### 1. BFS

•	En este caso, primero se expande el nodo raíz y luego todos los nodos generados por éste, luego sus sucesores y así sucesivamente. 

•	Todos los nodos que están a profundidad d se expanden antes que los nodos con profundidad d + 1.


### 2. DFS

•	En esta búsqueda siempre se expande uno de los nodos que se encuentre en lo más profundo del árbol. 

•	Sólo si la búsqueda conduce a un callejón sin salida (un nodo que no es meta y que no tiene expansión), se revierte la búsqueda y se expanden los nodos de niveles menos profundos.


# Análisis de Complejidad

### Algoritmo 01

O(n!)


### Algoritmo 02

O(n^3)


### Algoritmo 03

O(2^n)

# Conclusiones

•	El programa no llega a cargar todos los datos del archivo csv de donde se extrae la información.

•	Resulta difícil hacer que uno de los algoritmos implementados retorne el camino más corto, puesto que al crear las conexiones entre los centros poblados se hace de forma aleatoria.

•	El problema del Agente Viajero (TSP) es un problema cuya solución ha sido estudiada desde los inicios de la Inteligencia Artificial considerando que su aplicación puede ser en cualquier área de estudio cuyos problemas reflejen una situación donde se tienen diferentes puntos a visitar con un costo considerado en el enlace entre dichos puntos (costo: recursos empleados como distancia, tiempo, monto económico, etc.). Cada autor ha propuesto soluciones para ciertas instancias de TSP, cada uno con una perspectiva diferente empleando técnicas que no son repetibles pero que, en determinado momento, se pueden emplear para dar lugar a nuevas soluciones; de las técnicas empleadas la más común es el uso de redes neuronales dada su similitud, donde cada neurona es un nodo a visitar y las relaciones entre neuronas es el vector que representa el costo.


# Bibliografía

https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n3/e5.html
    
http://editorial.ucentral.edu.co/ojs_uc/index.php/Ingeciencia/article/download/310/277

https://networkx.github.io/documentation/networkx-2.3/tutorial.html
