
# Ejercicio 1. Investigación: Control de Versiones y Tecnologías de Desarrollo

## 1.1 ¿Qué es un Sistema de Control de Versiones?

Un **Sistema de Control de Versiones (VCS)** rastrea cada alteración realizada a un archivo o conjunto de archivos, lo que permite a los desarrolladores regresar a versiones anteriores y colaborar sin problemas.

- **Sistemas de Control de Versiones Centralizados (CVCS):** Optimizan el proceso al alojar todas las versiones de los archivos en un solo servidor. Los desarrolladores toman prestado un archivo para modificarlo y luego lo devuelven con actualizaciones, todo cuidadosamente almacenado y catalogado por el servidor. Ofrecen una vía directa y simple para gestionar los cambios.

- **Sistemas de Control de Versiones Distribuidos (DVCS):** A medida que los equipos crecen y los proyectos se vuelven más complejos, alternativas como **Git** pasan a primer plano. Un DVCS no solo centraliza los archivos, sino que los democratiza. Cada desarrollador posee todo el historial del proyecto a nivel local, lo que potencia el trabajo fuera de línea y facilita múltiples estrategias de ramificación y fusión.

---

## 1.2 Tipos de Sistemas de Control de Versiones

Los dos tipos más populares son los **centralizados** y los **distribuidos**, aunque existen otros enfoques como los basados en bloqueos y los optimistas.

### Distribuido (DVCS)

Permite a los usuarios acceder a un repositorio desde varias ubicaciones. Es utilizado por desarrolladores que necesitan trabajar desde múltiples computadoras o colaborar de forma remota.

### Centralizado (CVCS)

Todos los usuarios trabajan con el mismo repositorio central ubicado en un servidor o en una máquina local. Se utiliza comúnmente en equipos que comparten código y requieren un seguimiento unificado.

### Basado en Bloqueos

Utiliza el bloqueo de archivos para gestionar el acceso simultáneo, evitando que dos o más usuarios realicen cambios en conflicto sobre el mismo recurso.

### Optimista

Cada usuario trabaja en su propio espacio privado. Al querer compartir los cambios, envía una solicitud al servidor, el cual analiza la información y determina si la fusión se puede realizar de manera segura.

> **Problema concreto que resuelve:** evita la sobrescritura accidental de datos y el caos de los cambios incompatibles en el trabajo en equipo, mejorando la calidad del código, acelerando los plazos de desarrollo y aumentando la visibilidad del proyecto.

---

## 1.3 Herramientas principales: Git y GitHub

### Git

Es un sistema de control de versiones distribuido diseñado para seguir y gestionar los cambios en el código. Cada desarrollador trabaja con una copia local completa del proyecto para contribuir, confirmar (*commit*) y experimentar independientemente antes de sincronizar con el repositorio remoto.

- **Bifurcación (Branching):** permite trabajar en funciones de forma aislada sin alterar el código base principal.
- **Fusionar (Merge):** combina los cambios de código de distintas ramas.
- **Commits:** guarda instantáneas del código, creando una línea de tiempo del progreso.
- **Seguimiento del historial:** mantiene un registro detallado de cada cambio.

### GitHub

Es una plataforma en la nube para alojar repositorios Git. Permite a los equipos colaborar en una ubicación centralizada desde cualquier lugar.

- **Pull Requests:** permiten proponer, revisar y discutir cambios antes de fusionarlos.
- **Issues y Proyectos:** permiten gestionar errores, peticiones de funcionalidades y listas de tareas.
- **GitHub Actions:** permite automatizar pruebas, compilaciones y despliegues.
- **GitHub Pages:** permite alojar sitios web estáticos directamente desde un repositorio.
- **Herramientas de seguridad:** incluye mecanismos de autenticación, análisis de código y control de permisos.
- **GitHub Copilot:** proporciona asistencia para programación mediante inteligencia artificial.

### Comparativa: Git vs. GitHub

| Función | Git | GitHub |
|---|---|---|
| **Naturaleza** | Sistema de control de versiones | Plataforma de alojamiento para repositorios Git |
| **Ubicación** | Funciona localmente en la computadora | Servicio en línea |
| **Función principal** | Rastrea los cambios realizados en los archivos | Proporciona herramientas de colaboración y gestión de repositorios |
| **Interfaz** | Línea de comandos o clientes gráficos | Interfaz gráfica basada en web |
| **Elementos de seguridad** | El repositorio local no requiere autenticación por sí mismo | Admite autenticación de usuarios, permisos y control de acceso |
| **Alternativas** | SVN, Mercurial, Perforce | GitLab, Bitbucket, Azure DevOps |

---

## 1.4 Conceptos clave de un repositorio

- **Repositorio:** espacio donde se almacenan los archivos de un proyecto y su historial de modificaciones. Puede ser local o remoto.

- **`.gitignore`:** archivo de configuración que le indica a Git qué archivos o carpetas no debe rastrear, como archivos temporales, cachés o información que no debe formar parte del repositorio.

- **`README.md`:** archivo escrito normalmente en Markdown que presenta y documenta el proyecto. Puede incluir información sobre su objetivo, estructura, instalación y ejecución.

---

## 1.5 Contenedores y Virtualización

Un **contenedor** es una forma ligera de aislar y ejecutar aplicaciones junto con las bibliotecas y dependencias que necesitan. Los contenedores comparten el kernel del sistema operativo anfitrión, en lugar de ejecutar un sistema operativo invitado completo como ocurre normalmente con una máquina virtual.

Una de las plataformas más utilizadas para trabajar con contenedores es **Docker**.

### Diferencia entre Máquina Virtual y Contenedor

```text
+---------------------------------+     +---------------------------------+
|       Máquina Virtual (VM)      |     |           Contenedor            |
+---------------------------------+     +---------------------------------+
| Aplicación / Bibliotecas        |     | Aplicación / Bibliotecas        |
| Sistema Operativo Invitado      |     | Sin SO invitado completo        |
| Hipervisor                      |     | Motor de contenedores            |
| Sistema Operativo Anfitrión     |     | Sistema Operativo Anfitrión     |
| Hardware Físico                 |     | Hardware Físico                 |
+---------------------------------+     +---------------------------------+
```

---



# Ejercicio 2. Investigación: ¿Qué es la Teoría de la Computación?

## ¿Qué es la Teoría de la Computación?

La teoría de la computación es una rama de la informática que estudia las posibilidades y limitaciones de las computadoras. Busca comprender qué problemas pueden resolverse mediante algoritmos, cuáles no tienen una solución computacional y qué recursos se necesitan para resolverlos. Utiliza modelos matemáticos y herramientas lógicas que permiten analizar el funcionamiento de los sistemas computacionales.

### 1. Alan Turing

Alan Turing, en su trabajo *On Computable Numbers, with an Application to the Entscheidungsproblem* (1936), introdujo un modelo matemático conocido como **máquina de Turing**. A través de este modelo, sentó las bases para estudiar qué operaciones pueden realizarse mediante procedimientos mecánicos y cuáles son los límites de la computación.

Desde su perspectiva, podemos entender la computación como un proceso que sigue instrucciones definidas para manipular información. Su trabajo permite analizar si un procedimiento puede llevarse a cabo mediante una máquina y establecer límites matemáticos a lo que puede calcularse.

### 2. Christos H. Papadimitriou

Christos H. Papadimitriou, en su libro *Computational Complexity*, estudia los problemas computacionales teniendo en cuenta los recursos necesarios para resolverlos, especialmente el tiempo y la memoria.

Su enfoque permite comprender que no basta con saber si un problema puede resolverse: también es importante analizar cuánto esfuerzo computacional requiere encontrar una solución. De esta manera, se pueden estudiar las diferencias entre problemas que se resuelven con pocos recursos y aquellos que necesitan una cantidad considerable de ellos.

---

## ¿Qué preguntas se plantea la Teoría de la Computación?

La teoría de la computación intenta responder preguntas que ayudan a comprender el alcance de los sistemas computacionales. Entre las principales se encuentran:

- ¿Todos los problemas pueden resolverse mediante una computadora o existen algunos que están fuera de sus capacidades?
- ¿Cómo podemos demostrar que un problema puede resolverse mediante un algoritmo?
- ¿Qué características debe tener un procedimiento para considerarse computable?
- ¿Cuánto tiempo y memoria necesita una computadora para resolver un problema?
- ¿Por qué algunos problemas requieren muchos más recursos que otros?
- ¿Qué modelos matemáticos permiten representar el funcionamiento de una computadora?
- ¿Cómo podemos identificar las limitaciones de un sistema computacional antes de intentar resolver un problema?

---

## Comparación de las definiciones

Las perspectivas de Turing y Papadimitriou se relacionan porque ambas contribuyen a comprender las capacidades de la computación, aunque se concentran en aspectos diferentes.

Turing proporciona las bases para estudiar si un problema puede resolverse mediante un procedimiento computacional. Su trabajo permite establecer qué puede calcular una máquina y reconocer que existen problemas que no pueden solucionarse mediante algoritmos.

Por su parte, Papadimitriou se concentra en analizar los recursos que requiere la resolución de los problemas; su enfoque permite estudiar la eficiencia de los algoritmos y comprender por qué algunos problemas son más costosos de resolver que otros.

Por lo tanto, ambos enfoques se complementan: **Turing ayuda a entender si un problema puede resolverse, mientras que Papadimitriou permite analizar los recursos necesarios para hacerlo.**

---

## Sus orígenes: el programa de Hilbert, el Entscheidungsproblem y las paradojas de la lógica matemática

Los orígenes de la teoría de la computación se relacionan con una serie de dificultades que surgieron en las matemáticas y la lógica a finales del siglo XIX y principios del siglo XX.

En esa época, varios matemáticos buscaban establecer reglas precisas que permitieran fundamentar las matemáticas y determinar si los razonamientos podían verificarse mediante procedimientos formales.

### 1. El programa de Hilbert

David Hilbert fue un matemático que propuso un programa para darles a las matemáticas una base lógica y rigurosa. Lo que buscaba era expresar las teorías matemáticas mediante sistemas de axiomas y demostrar que estos sistemas eran consistentes, es decir, que no permitían obtener contradicciones.

También buscaba establecer métodos formales que permitieran comprobar los resultados matemáticos. Este proyecto fue importante porque planteó la posibilidad de estudiar los razonamientos matemáticos de manera sistemática, utilizando reglas definidas.

Sin embargo, los resultados posteriores de Kurt Gödel demostraron que existían límites fundamentales para alcanzar todos los objetivos de Hilbert mediante un sistema formal.

### 2. El Entscheidungsproblem

El *Entscheidungsproblem*, cuyo nombre en alemán significa **problema de decisión**, fue una pregunta planteada por Hilbert y Wilhelm Ackermann en 1928.

Consistía en determinar si existía un procedimiento mecánico y general que permitiera decidir, en una cantidad finita de pasos, si una fórmula de la lógica de primer orden era válida.

Este problema tuvo una importancia especial para el desarrollo de la computación porque planteaba una pregunta fundamental: ¿es posible crear un algoritmo que resuelva automáticamente cualquier problema de este tipo?

En 1936, Alan Turing y Alonzo Church demostraron, mediante enfoques diferentes, que no existe un procedimiento general que resuelva el problema de decisión para toda la lógica de primer orden. Estos resultados contribuyeron a establecer los límites de lo que puede calcularse mediante algoritmos.

### 3. Las paradojas de la lógica matemática

Las paradojas también desempeñaron un papel importante en el desarrollo de los fundamentos de la computación. A finales del siglo XIX y principios del XX, los matemáticos encontraron contradicciones relacionadas con ciertos sistemas lógicos y con la teoría de conjuntos.

Un ejemplo conocido es la **paradoja de Russell**, presentada por Bertrand Russell en 1901. Esta paradoja mostraba dificultades en una concepción de los conjuntos que permitía considerar libremente cualquier colección de objetos como un conjunto.

El problema evidenció la necesidad de establecer reglas más cuidadosas para evitar contradicciones. Estas dificultades impulsaron el desarrollo de sistemas axiomáticos y métodos formales más rigurosos; además, motivaron investigaciones sobre la consistencia, la demostración y los límites de los sistemas matemáticos.

---

## Relación entre estos acontecimientos y la Teoría de la Computación

Los tres temas están conectados porque surgieron de una preocupación común: **determinar hasta dónde es posible formalizar y resolver problemas matemáticos mediante reglas precisas.**

- El programa de Hilbert buscaba establecer fundamentos rigurosos para las matemáticas.
- El *Entscheidungsproblem* preguntaba si existía un método general para decidir la validez de las fórmulas lógicas.
- Las paradojas mostraron que algunos sistemas matemáticos necesitaban fundamentos más sólidos para evitar contradicciones.

Posteriormente, los trabajos de Gödel, Turing y Church permitieron comprender que existen límites tanto en lo que los sistemas formales pueden demostrar como en lo que los algoritmos pueden resolver.

Estas investigaciones sentaron bases importantes para la teoría de la computación, especialmente para el estudio de la computabilidad y de los problemas que no pueden solucionarse mediante procedimientos algorítmicos.

---

## ¿Qué afirma la tesis de Church-Turing?

La tesis de Church-Turing plantea que todo cálculo que pueda realizarse siguiendo un método efectivo de instrucciones también puede ser llevado a cabo por una **máquina de Turing**.

En otras palabras, propone que, si existe un procedimiento mecánico para obtener el resultado de un cálculo, ese procedimiento puede representarse mediante este modelo matemático.

Esta idea surgió durante la década de 1930, cuando Alan Turing y Alonzo Church investigaban si era posible establecer un método general para resolver problemas matemáticos. Aunque cada uno utilizó un enfoque diferente, sus investigaciones llegaron a una conclusión relacionada: la computación tiene límites y no todos los problemas pueden resolverse mediante algoritmos.

Lo interesante de esta tesis es que permite estudiar la computación sin depender de una computadora física específica. En lugar de preguntarnos qué puede hacer una computadora moderna, podemos analizar matemáticamente qué operaciones son posibles mediante un procedimiento efectivo.

---

## ¿Qué modelos de computación se demostraron equivalentes?

Una parte importante del desarrollo de esta teoría fue descubrir que algunos modelos computacionales, a pesar de tener estructuras muy diferentes, poseen la misma capacidad de cálculo.

Entre ellos se encuentran los siguientes:

- **Máquinas de Turing:** representan los cálculos mediante una máquina abstracta que lee y escribe símbolos siguiendo instrucciones determinadas.
- **Cálculo lambda:** desarrollado por Alonzo Church, expresa los cálculos mediante funciones y operaciones de sustitución. En lugar de utilizar una cinta como la máquina de Turing, trabaja con expresiones matemáticas.
- **Funciones recursivas generales:** describen los cálculos mediante funciones definidas a partir de reglas matemáticas y procedimientos de recursión.
- **Funciones $\mu$-recursivas:** utilizan operaciones como la composición, la recursión y la minimización para construir funciones computables.

La equivalencia entre estos modelos significa que pueden calcular la misma clase de funciones, aunque cada uno represente el proceso de una manera distinta.

### La tesis de Church-Turing

Se llama *tesis* porque no es un teorema matemático convencional que pueda demostrarse a partir de un conjunto de axiomas.

La dificultad está en el significado de la expresión *procedimiento efectivo*: esta expresión se refiere intuitivamente a un método que puede seguirse de manera precisa y mecánica, pero no constituye por sí misma una definición matemática formal.

Church y Turing propusieron modelos matemáticos que permiten representar esa idea; la tesis sostiene que dichos modelos abarcan todos los procedimientos que intuitivamente consideraríamos algoritmos efectivos.

Es importante distinguir dos cuestiones: la equivalencia entre los modelos formales puede demostrarse matemáticamente, pero la afirmación de que estos modelos representan todos los procedimientos efectivos es lo que constituye la tesis.

---

# Conceptos Fundamentales

## Alfabeto

Un alfabeto, representado normalmente por la letra griega $\Sigma$ (sigma), es un conjunto finito y no vacío de símbolos que se utilizan para formar cadenas.

## Cadena

Una cadena es una secuencia finita de símbolos pertenecientes a un alfabeto. Su longitud se representa mediante:

$$
|w|
$$

donde $w$ es la cadena.

## Lenguaje

Un lenguaje formal es cualquier conjunto de cadenas construidas a partir de un alfabeto determinado.

## Concatenación de cadenas

La concatenación consiste en colocar una cadena inmediatamente después de otra, sin agregar separaciones.

## Potencia de una cadena

La potencia de una cadena consiste en concatenarla consigo misma una cantidad determinada de veces:

$$
w^n
$$

## Reflexión de una cadena

La reflexión, también llamada reversión, consiste en escribir los símbolos de una cadena en orden inverso. Se representa mediante:

$$
w^R
$$

## Concatenación de lenguajes

La concatenación de dos lenguajes $L_1L_2$ consiste en concatenar cada cadena del primer lenguaje con cada cadena del segundo.

## Unión

La unión:

$$
L_1 \cup L_2
$$

reúne las cadenas que pertenecen a uno u otro lenguaje, incluyendo las que aparecen en ambos.

## Intersección

La intersección:

$$
L_1 \cap L_2
$$

contiene únicamente las cadenas que pertenecen simultáneamente a los dos lenguajes.

## Diferencia

La diferencia:

$$
L_1-L_2
$$

contiene las cadenas que pertenecen al primer lenguaje, pero no al segundo.

## Reflexión de un lenguaje

La reflexión de un lenguaje:

$$
L^R
$$

consiste en invertir cada una de las cadenas que lo componen.

## Cerradura de Kleene

La cerradura de Kleene de un lenguaje $L$, representada por $L^*$, contiene todas las cadenas que pueden formarse concatenando cero o más cadenas pertenecientes a $L$.

## Cerradura positiva

La cerradura positiva de un lenguaje $L$, representada por $L^+$, contiene todas las cadenas que pueden formarse concatenando una o más cadenas de $L$.

---

## ¿Por qué $\Sigma^*$ y qué distingue a $\Sigma^+$?

$\Sigma^*$ representa el conjunto de cadenas que se obtienen concatenando cero o más símbolos del alfabeto.

Cuando no se selecciona ningún símbolo, el resultado es la **cadena vacía** ($\epsilon$ o $\lambda$).

Aunque ambas expresiones representan conjuntos de cadenas construidas a partir de un alfabeto, se diferencian en la longitud mínima permitida:

- **$\Sigma^*$:** contiene todas las cadenas finitas que pueden construirse con símbolos del alfabeto, **incluyendo la cadena vacía**.
- **$\Sigma^+$:** contiene todas las cadenas finitas **no vacías** que pueden construirse con símbolos del alfabeto.

Por lo tanto:

$$
\Sigma^+ = \Sigma^* - \{\epsilon\}
$$

---

# Jerarquía de Chomsky

La jerarquía de Chomsky es una clasificación de las gramáticas formales propuesta por Noam Chomsky en 1956.

Organiza las gramáticas en cuatro niveles, de acuerdo con las restricciones que tienen sus reglas de producción y la capacidad de los mecanismos computacionales necesarios para reconocer los lenguajes que generan.

| Tipo | Nombre de la gramática | Forma de las producciones | Lenguaje generado | Máquina que lo reconoce |
|---|---|---|---|---|
| **Tipo 0** | Gramática no restringida | $\alpha \rightarrow \beta$, donde $\alpha \neq \epsilon$ | Lenguajes recursivamente enumerables | Máquina de Turing |
| **Tipo 1** | Gramática sensible al contexto | $\alpha A \beta \rightarrow \alpha \gamma \beta$, donde $\gamma \neq \epsilon$ | Lenguajes sensibles al contexto | Autómata linealmente acotado (LBA) |
| **Tipo 2** | Gramática independiente del contexto | $A \rightarrow \gamma$, donde $A$ es un único no terminal | Lenguajes independientes del contexto | Autómata de pila (PDA) |
| **Tipo 3** | Gramática regular | $A \rightarrow aB$, $A \rightarrow a$ o $A \rightarrow \lambda$ | Lenguajes regulares | AFD o AFN |

> Esto significa que todo lenguaje regular también es independiente del contexto, todo lenguaje independiente del contexto es sensible al contexto y todo lenguaje sensible al contexto es recursivamente enumerable.

---

# Autómatas Finitos

## 1. Definición formal del AFD

Un **autómata finito determinista (AFD)** es un modelo matemático que procesa una cadena símbolo por símbolo y cambia de estado siguiendo reglas previamente establecidas.

Se llama determinista porque nunca tiene que elegir entre varias transiciones posibles: para cada símbolo que lee desde un estado, existe una única transición definida.

Formalmente, se representa mediante una quíntupla:

$$
M=(Q,\Sigma,\delta,q_0,F)
$$

Donde:

- **$Q$:** conjunto finito de estados.
- **$\Sigma$:** alfabeto de entrada.
- **$\delta$:** función de transición.

$$
\delta:Q\times\Sigma\rightarrow Q
$$

- **$q_0$:** estado inicial, donde $q_0\in Q$.
- **$F$:** conjunto de estados finales o de aceptación, donde $F\subseteq Q$.

## 2. Definición formal del AFN

Un **autómata finito no determinista (AFN)** también reconoce cadenas, pero permite que desde un estado existan varias transiciones posibles para un mismo símbolo.

Incluso puede no existir ninguna transición para determinada combinación de estado y símbolo.

Se define formalmente como:

$$
M=(Q,\Sigma,\delta,q_0,F)
$$

Sus componentes son los mismos que los de un AFD, pero su función de transición cambia:

$$
\delta:Q\times\Sigma\rightarrow\mathcal{P}(Q)
$$

Aquí, $\mathcal{P}(Q)$ es el conjunto potencia de $Q$. Esto significa que una transición puede conducir a un conjunto de estados, en lugar de conducir obligatoriamente a uno solo.

En un AFN con transiciones $\epsilon$, también se permiten movimientos que no consumen símbolos de entrada.

Una cadena se acepta si al menos uno de los caminos posibles termina en un estado final después de consumir toda la cadena.

**Ejemplo:** un sistema que busca la aparición de la secuencia `101` dentro de una cadena binaria podría utilizar un AFN que mantenga distintas posibilidades sobre dónde comienza esa secuencia; si alguno de los caminos logra reconocerla, la cadena puede aceptarse.

## 3. Equivalencia entre AFD y AFN

Aunque el AFD y el AFN tienen distintas formas de procesar la información, ambos pueden reconocer exactamente la misma clase de lenguajes: **los lenguajes regulares**.

La diferencia está en la manera de representar las posibilidades durante el procesamiento. El AFD mantiene un único estado activo, mientras que el AFN puede considerar varios estados posibles.

Para demostrar su equivalencia se utiliza una técnica llamada **construcción por subconjuntos**, que consiste en construir un AFD cuyos estados representan conjuntos de estados del AFN original.

Así, el AFD puede representar en un solo estado todas las alternativas que el AFN podría seguir. El no determinismo puede facilitar la construcción de un autómata, pero no le permite reconocer lenguajes que estén fuera de las capacidades de los autómatas deterministas.

---

# Tres problemas reales en los que se aplican las expresiones regulares

Las expresiones regulares permiten describir patrones de texto mediante símbolos y operadores. Su utilidad se aprecia especialmente cuando un sistema necesita revisar grandes cantidades de información siguiendo criterios específicos.

## Problema 1: Detectar códigos de seguimiento mal escritos

Una empresa de mensajería utiliza códigos con el formato:

```text
MX-2026-5831
```

Cuando un usuario introduce un código, el sistema necesita comprobar que tenga dos letras mayúsculas, un guion, cuatro dígitos, otro guion y cuatro dígitos.

Una expresión regular para comprobar ese formato sería:

```regex
^[A-Z]{2}-[0-9]{4}-[0-9]{4}$
```

## Problema 2: Encontrar errores específicos en los registros de un servidor

Cuando una página web presenta fallos, el servidor puede generar miles de líneas de registro. Revisarlas manualmente puede llevar mucho tiempo.

Si el equipo técnico necesita localizar las líneas que contienen errores HTTP 500, puede utilizar una expresión regular que busque ese código en el formato utilizado por sus registros.

Por ejemplo, si cada línea contiene el código de estado entre espacios:

```regex
\s500\s
```

Esto permite localizar coincidencias con el código `500` rodeado de espacios. El patrón tendría que ajustarse si el registro utiliza otro formato.

De esta manera, las expresiones regulares ayudan a filtrar información y facilitan la investigación de problemas técnicos.

## Problema 3: Extraer identificadores de facturas de documentos

Un sistema de contabilidad recibe documentos que incluyen identificadores como:

```text
FAC-2026-0184
```

Para organizar las facturas, necesita localizar esos identificadores dentro del texto.

Puede utilizar la siguiente expresión regular:

```regex
FAC-[0-9]{4}-[0-9]{4}
```

El patrón reconoce la palabra `FAC-`, seguida de cuatro dígitos, otro guion y cuatro dígitos.

Esto permite reunir los identificadores encontrados y utilizarlos en procesos posteriores, como la clasificación o la búsqueda de documentos. Si se necesita confirmar que una factura es auténtica, el sistema deberá comprobar también su información en los registros correspondientes.