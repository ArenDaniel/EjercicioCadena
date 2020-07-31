
![chain of responsibility](imagenes/chainofresponsibility.png)

- **Ejercicio:** Modificar el repositorio con los ejemplos de patrones de tal modo que su ejecucion funcionara con el patron "Cadena de responsabilidad" (Chain of responsabilitiy).

La estrucutura del patron.

**Handler/Manejador:**
El Handler es la clase manejador, esta clase es la que nos crea en enlace entre los manejadores concretos, los cuales tiene como operacion ejecutar el patron correspondiente.

**Manejadores Concretos:**
Cada manejador concreto (Expresado como ManejadorUno,ManejadorDos) tiene la operacion Manejador_Request. Esta funcion compara la opcion que dio el usuario, en caso de considir ejecuta el patron correspodiente, en caso contrario se ecuta la misma funcion pero con su sucesor.

**Sucesor**:
El sucesor es asignado en la clase manejador, y en la operacion con el cliente. Este sucesor se asigna instanciando cada manejador concreto.




**Daniel Arenas Ejercicio Cadena de Responsabilidad**


