# meteologica
Repositorio en el que la empresa Meteologica solicitó, en su segunda fase del proceso de selección para vacante de programador C++/Perl/Python, la realización de al menos uno de los 3 ejercicios propuestos vía mail. 

El ejercicio elegido fue el número 3 con el siguiente enunciado:

Construcción económica de vallas

Tenemos algunos bosques por el campo, y queríamos construir una valla alrededor para que no entre ningún pirómano. Cada uno de esos bosques tiene los árboles distribuidos de forma irregular, y queremos vallarlos de la forma más económica posible, es decir, minimizando la longitud total de la valla. El ejercicio consiste en hacer un pequeño programa que dada una serie de puntos nos devuelve el polígono que corresponderá a la valla (basta con los vértices de ese polígono).

Este ejercicio ha sido desarrollado en Python con las siguiente librerías de open source:
 - Numpy
 - Pandas
 - Matplotlib
 - Math
 - Random
 
Para la resolución de este ejercicio, se han calculado las pendientes de las rectas de los puntos (árboles), de forma que, el ángulo mayor (recta con mayor pendiente) es el siguiente punto del perímetro. Resaltar, que para la correcta selección de la mayor pendiente, se deben hallar, primero, los cuadrantes en los que están ubicados los puntos comprobando las inclinaciones por ese orden.

Por último, la comprobación del perímetro se realiza con una visualización en terminal.
