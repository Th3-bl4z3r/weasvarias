# 📘 MÓDULO 1: FUNDAMENTOS DE C++
## Tipos de Datos, Variables y Control de Flujo

**Duración sugerida:** 90-120 minutos  
**Prerequisitos:** Conocimiento de compuertas lógicas, álgebra booleana, assembler básico  
**Objetivo:** Comprender cómo se representan datos en memoria y cómo el compilador traduce C++ a máquina

---

## 📑 Tabla de Contenidos

1. [Introducción: De Matemáticas a Memoria](#introducción-de-matemáticas-a-memoria)
2. [Tipos de Datos Primitivos](#tipos-de-datos-primitivos)
3. [Variables y Almacenamiento en Memoria](#variables-y-almacenamiento-en-memoria)
4. [Operadores y Expresiones](#operadores-y-expresiones)
5. [Control de Flujo](#control-de-flujo)
6. [Análisis Línea por Línea: Tu Primer Programa](#análisis-línea-por-línea-tu-primer-programa)
7. [Desafíos del Módulo 1](#desafíos-del-módulo-1)

---

## 🎯 Introducción: De Matemáticas a Memoria

Cuando escribes en Python:
```python
x = 5
```

Es simple: `x` es una variable que contiene `5`.

Pero en **C++**, esa línea es profundamente diferente. Aquí tienes que **especificar exactamente cómo se almacena ese número en la memoria física de tu computador**.

### ¿Por qué? Contexto Histórico y Técnico

**Python** es de **alto nivel**: el lenguaje decide por ti cómo almacenar datos.

**C/C++** es de **bajo nivel**: TÚ decides cómo se almacenan, cuánta memoria usan, y cómo se manipulan en bits.

Esto es crucial porque:
- Escritura en assembler → escribes instrucciones directas a la CPU
- Escritura en C++ → escribes instrucciones que el compilador traduce a assembler
- **Compilador** = programa que traduce C++ a código máquina

---

## 🔢 Tipos de Datos Primitivos

### ¿Qué es un "tipo de dato"?

Un **tipo de dato** es una especificación que le dice al compilador:
1. **Cuántos bytes de memoria reservar**
2. **Cómo interpretar esos bytes** (¿como número? ¿como carácter? ¿positivo o negativo?)
3. **Qué operaciones son válidas**

### Tabla de Tipos Primitivos en C++

| Tipo | Tamaño (bytes) | Rango | Caso de Uso |
|------|---|---|---|
| `char` | 1 | -128 a 127 (o 0-255 sin signo) | Caracteres individuales, códigos ASCII |
| `short` | 2 | -32,768 a 32,767 | Números pequeños |
| `int` | 4 | ~-2.1 millones a 2.1 millones | Números enteros estándar |
| `long` | 4 u 8 | Más grande que int | Números muy grandes |
| `float` | 4 | Decimales con ~6 dígitos precisión | Números reales rápidos |
| `double` | 8 | Decimales con ~15 dígitos precisión | Números reales precisos (default) |
| `bool` | 1 | `true` (1) o `false` (0) | Valores booleanos |

### Profundización: Representación en Memoria

Cuando declaras `int x = 5;`, aquí sucede:

#### Paso 1: El Compilador Reserva 4 Bytes
```
Dirección de memoria:  0x1000   0x1001   0x1002   0x1003
Contenido (binario):   00000000 00000000 00000000 00000101
                       └─────────────────────────────────┘
                              Valor: 5 en decimal
```

#### Paso 2: El Compilador Recuerda la Dirección
```
Variable 'x' → dirección de memoria 0x1000
```

Cuando escribes `x`, el compilador automáticamente busca en `0x1000` y obtiene los 4 bytes.

#### Paso 3: Operaciones Respetan el Tipo
```cpp
int x = 5;
int y = x + 3;  // El compilador sabe que suma dos INT
```

El compilador genera una instrucción assembler tipo:
```asm
ADD [0x1000], 3  ; suma 3 al contenido en dirección 0x1000
```

---

### Ejemplo: Diferencia Entre Tipos

```cpp
char a = 5;    // Reserva 1 byte: 00000101
int b = 5;     // Reserva 4 bytes: 00000000 00000000 00000000 00000101
```

**Ambos almacenan 5**, pero `int` usa 4 veces más memoria. ¿Cuándo importa?

- Programa pequeño: no importa
- Programa con millones de números: importa MUCHO
- Dispositivo embebido con 2KB de RAM: **crítico**

---

### Números Negativos: Complemento a Dos

¿Cómo almacena C++ números negativos?

Usa **complemento a dos** (estándar en computadores):

```
Número positivo 5:   00000101
Número negativo -5:  11111011
```

**¿Cómo funciona?**
1. Invierte todos los bits de 5: `00000101` → `11111010`
2. Suma 1: `11111010` + 1 → `11111011`

Ventaja: La suma funciona igual para positivos y negativos:
```
  00000101  (+5)
+ 11111011  (-5)
-----------
 100000000  (0, se descarta el bit extra)
```

---

### Números Decimales: IEEE 754

`float` y `double` usan el estándar **IEEE 754**. Almacenan números como:

```
[signo (1 bit)] [exponente (8 bits)] [mantisa (23 bits)]
```

Ejemplo: `3.5` se almacena aproximadamente como:
```
0 10000000 11000000000000000000000
```

**Importante:** No todos los decimales se pueden representar exactamente (ej: 0.1):

```cpp
double x = 0.1;
cout << x;  // Imprime: 0.1 (pero internamente es 0.1000000000000000055...)
```

Por eso en ciencia computacional usamos `epsilon` para comparar decimales:
```cpp
if (abs(x - 0.1) < 1e-9) {
    // Se considera "igual a 0.1"
}
```

---

## 💾 Variables y Almacenamiento en Memoria

### Declaración vs. Definición vs. Asignación

Estos términos son CRUCIALES en C++:

#### Declaración
```cpp
int x;  // Le dices al compilador: "existe una variable int llamada x"
```
**Qué sucede:** El compilador RESERVA 4 bytes de memoria para `x`.  
**Contenido:** DESCONOCIDO (basura, valor anterior en esa memoria).

#### Inicialización (Declaración + Asignación)
```cpp
int x = 5;  // Declara y asigna simultáneamente
```
**Qué sucede:** Reserva 4 bytes Y escribe 5 en ellos.

#### Asignación (sin declaración)
```cpp
x = 10;  // Asigna 10 a la variable existente x
```
**Qué sucede:** Sobrescribe el contenido de esos 4 bytes con 10.

### Diferencia Crítica en C++

En **Python:**
```python
x = 5  # Se crea automáticamente
print(x)  # Funciona
```

En **C++:**
```cpp
x = 5;  // ERROR: ¿cuál es x? Nunca fue declarada
int x = 5;  // Bien: declara e inicializa
cout << x;  // Funciona
```

**¿Por qué C++ es así?** Porque en sistemas de bajo nivel, cada byte cuenta. C++ quiere que seas **explícito** sobre cuánta memoria usas.

---

### Scope (Alcance) de Variables

```cpp
int main() {
    int x = 5;      // x existe aquí
    
    {
        int y = 10; // y existe solo en este bloque
        cout << x;  // Bien: x es accesible
        cout << y;  // Bien: y es accesible
    }
    
    cout << y;      // ERROR: y no existe fuera de su bloque
    return 0;
}
```

**Regla:** Una variable existe desde donde se declara hasta el final del bloque `{}` más cercano.

---

## 🔧 Operadores y Expresiones

### Operadores Aritméticos

| Operador | Símbolo | Ejemplo | Resultado |
|---|---|---|---|
| Suma | `+` | `5 + 3` | `8` |
| Resta | `-` | `5 - 3` | `2` |
| Multiplicación | `*` | `5 * 3` | `15` |
| División | `/` | `7 / 2` | `3` (enteros truncan) |
| Módulo | `%` | `7 % 2` | `1` |

**Cuidado División Entera:**
```cpp
int a = 7;
int b = 2;
int resultado = a / b;  // resultado = 3, no 3.5
```

Si quieres decimales:
```cpp
double resultado = (double)a / b;  // Casteo: convierte a double
// resultado = 3.5
```

---

### Operadores Lógicos (Conexión con Álgebra Booleana)

Recuerda compuertas lógicas del curso de CS1. En C++ se expresan así:

| Operador | Símbolo | Tabla de Verdad |
|---|---|---|
| AND | `&&` | `true && true = true`, resto `false` |
| OR | `\|\|` | `false \|\| false = false`, resto `true` |
| NOT | `!` | `!true = false`, `!false = true` |

**Ejemplo:**
```cpp
bool tiene_dinero = true;
bool es_mayor_edad = true;

if (tiene_dinero && es_mayor_edad) {
    cout << "Puede comprar cerveza (en países con restricción)";
}
```

**Cortocircuito (Lazy Evaluation):**
```cpp
if (false && funcion_costosa()) {
    // funcion_costosa() NUNCA se ejecuta
    // porque false && anything = false
}
```

Esto es IMPORTANTE para eficiencia.

---

### Operadores Bitwise (Conexión con Compuertas Lógicas)

Estos operan directamente en BITS. Recuerdas compuertas NOT, AND, OR, XOR del curso anterior:

| Operador | Símbolo | Descripción |
|---|---|---|
| AND bitwise | `&` | AND bit a bit |
| OR bitwise | `\|` | OR bit a bit |
| XOR bitwise | `^` | XOR bit a bit |
| NOT bitwise | `~` | NOT bit a bit |
| Desplazar izq | `<<` | Multiplica por 2^n |
| Desplazar der | `>>` | Divide por 2^n |

**Ejemplo práctico:**
```cpp
int a = 5;      // Binario: 0101
int b = 3;      // Binario: 0011

int resultado = a & b;  // AND: 0101 & 0011 = 0001 = 1
```

**Desplazamiento (Shift):**
```cpp
int x = 4;          // Binario: 0100
int resultado = x << 1;  // 01000 = 8 (4 * 2)
resultado = x >> 1;      // 0010 = 2 (4 / 2)
```

Esto es RAPIDÍSIMO a nivel de CPU. Prueba esto:
```cpp
// En vez de multiplicar por 2:
y = x * 2;      // Lento

// Usa shift:
y = x << 1;     // Rápido (directamente en CPU)
```

---

### Operadores de Comparación

| Operador | Símbolo | Resultado |
|---|---|---|
| Igual | `==` | Retorna `true` si son iguales |
| No igual | `!=` | Retorna `true` si son diferentes |
| Menor | `<` | Retorna `true` si izq < der |
| Menor o igual | `<=` | Retorna `true` si izq ≤ der |
| Mayor | `>` | Retorna `true` si izq > der |
| Mayor o igual | `>=` | Retorna `true` si izq ≥ der |

**Ejemplo:**
```cpp
int edad = 18;

if (edad >= 18) {
    cout << "Eres mayor de edad";
}
```

---

## 🔄 Control de Flujo

### if / else if / else

**Estructura:**
```cpp
if (condición1) {
    // Código si condición1 es true
} else if (condición2) {
    // Código si condición1 es false Y condición2 es true
} else {
    // Código si todas las anteriores son false
}
```

**Ejemplo:**
```cpp
int edad = 25;

if (edad < 13) {
    cout << "Eres niño";
} else if (edad < 18) {
    cout << "Eres adolescente";
} else if (edad < 65) {
    cout << "Eres adulto";
} else {
    cout << "Eres adulto mayor";
}
```

---

### Bucles: while

**Estructura:**
```cpp
while (condición) {
    // Código que se repite mientras condición sea true
}
```

**Flujo:**
1. Evalúa la condición
2. Si es `true`, ejecuta el bloque
3. Vuelve a paso 1
4. Si es `false`, sale del bucle

**Ejemplo:**
```cpp
int contador = 0;

while (contador < 5) {
    cout << contador << " ";
    contador++;
}
// Imprime: 0 1 2 3 4
```

**Cuidado: Bucle Infinito**
```cpp
int x = 0;
while (x < 10) {
    cout << x;
    // OLVIDASTE: x++
    // El bucle nunca termina
}
```

---

### Bucles: for

**Estructura:**
```cpp
for (inicialización; condición; actualización) {
    // Código que se repite
}
```

Es equivalente a:
```cpp
inicialización;
while (condición) {
    // Código
    actualización;
}
```

**Ejemplo:**
```cpp
for (int i = 0; i < 5; i++) {
    cout << i << " ";
}
// Imprime: 0 1 2 3 4
```

**¿Cuándo usar `for` vs `while`?**
- `for`: Cuando **sabes cuántas iteraciones** necesitas
- `while`: Cuando **no sabes cuántas iteraciones** (ej: leer hasta EOF)

---

### break y continue

**break:** Sale del bucle
```cpp
for (int i = 0; i < 10; i++) {
    if (i == 5) break;  // Sale cuando i = 5
    cout << i << " ";
}
// Imprime: 0 1 2 3 4
```

**continue:** Salta a la siguiente iteración
```cpp
for (int i = 0; i < 5; i++) {
    if (i == 2) continue;  // Salta cuando i = 2
    cout << i << " ";
}
// Imprime: 0 1 3 4
```

---

## 🔍 Análisis Línea por Línea: Tu Primer Programa

Ahora vamos a diseccionar el `main.cpp` que compilaste:

```cpp
#include <iostream>
using namespace std;

int suma(int a, int b) {
    return a + b;
}

int main() {
    int x = 5;
    int y = 3;
    int resultado = suma(x, y);
    
    cout << "x = " << x << endl;
    cout << "y = " << y << endl;
    cout << "La suma de x y y es: " << resultado << endl;
    
    return 0;
}
```

### Línea 1: `#include <iostream>`

**¿Qué es?** Directiva de preprocesador.

**¿Qué hace?** Le dice al compilador: "Incluye el archivo `iostream` antes de compilar".

`iostream` = "input output stream" = biblioteca de entrada/salida

Contiene definiciones de `cout` (output), `cin` (input), `endl` (end line).

Sin esta línea:
```cpp
cout << "Hola";  // ERROR: cout no está definido
```

---

### Línea 2: `using namespace std;`

**¿Qué es?** Declaración de namespace.

**¿Qué hace?** Sin esta línea tendrías que escribir:
```cpp
std::cout << "Hola";  // Con el prefijo std::
```

Con `using namespace std;` escribes:
```cpp
cout << "Hola";  // Sin prefijo
```

**Razón:** C++ tiene "espacios de nombres" para evitar conflictos (ej: dos librerías con función `suma`).

---

### Línea 4-6: Definición de Función

```cpp
int suma(int a, int b) {
    return a + b;
}
```

**Desglose:**
- `int`: tipo de retorno (la función devuelve un `int`)
- `suma`: nombre de la función
- `(int a, int b)`: parámetros (recibe dos `int`)
- `return a + b;`: retorna la suma

**En memoria:**
```
Cuando llamas suma(5, 3):
1. Se reservan 4 bytes para 'a', se escribe 5
2. Se reservan 4 bytes para 'b', se escribe 3
3. Se calcula: 5 + 3 = 8
4. Se retorna 8
5. Se liberan 'a' y 'b' (su memoria se reutiliza)
```

---

### Línea 9-10: Declaración de Variables

```cpp
int x = 5;
int y = 3;
```

En memoria (línea 9):
```
Dirección: 0x1000   0x1001   0x1002   0x1003
Valor:     00000000 00000000 00000000 00000101
           └─────────────────────────────────┘
                   x = 5
```

En memoria (línea 10):
```
Dirección: 0x1004   0x1005   0x1006   0x1007
Valor:     00000000 00000000 00000000 00000011
           └─────────────────────────────────┘
                   y = 3
```

---

### Línea 11: Llamada a Función y Asignación

```cpp
int resultado = suma(x, y);
```

**Pasos en tiempo de ejecución:**
1. Crea variable `resultado` (reserva 4 bytes)
2. Evalúa `suma(x, y)`:
   - Pasa 5 y 3 a la función
   - Función calcula 5 + 3 = 8
   - Función retorna 8
3. Asigna 8 a `resultado`

---

### Línea 13-15: Salida (cout)

```cpp
cout << "x = " << x << endl;
```

**¿Qué es `<<`?** Operador de inserción (flujo). Significa "envía a la salida".

Se lee de izquierda a derecha:
1. `cout`: flujo de salida estándar (pantalla)
2. `<<`: envía al flujo
3. `"x = "`: cadena de texto
4. `<<`: envía al flujo
5. `x`: valor de x (5)
6. `<<`: envía al flujo
7. `endl`: salto de línea

Resultado en pantalla:
```
x = 5
```

---

### Línea 20: `return 0;`

En `main()`, `return 0;` significa:
- **Éxito:** El programa terminó sin errores
- Otros valores (1, 2, etc.) indican error

El Sistema Operativo usa esto para saber si el programa funcionó.

---

## 🎯 Desafíos del Módulo 1

### Desafío 1: Conversor de Temperaturas

**Dificultad:** ⭐⭐ (Moderada)

**Problema:**
Escribe un programa que convierta temperaturas entre Celsius y Fahrenheit.

**Requisitos:**
1. El programa debe PEDIR al usuario que ingrese una temperatura en Celsius
2. Convertir a Fahrenheit usando la fórmula: `F = (C × 9/5) + 32`
3. Mostrar ambas temperaturas con 2 decimales de precisión
4. Validar que la temperatura no sea menor a -273.15°C (cero absoluto)

**Entrada esperada:**
```
Ingrese temperatura en Celsius: 25
```

**Salida esperada:**
```
Temperatura: 25°C = 77°F
```

**Casos especiales a considerar:**
- Temperatura negativa (ej: -40°C)
- Temperatura en cero absoluto (ej: -273.15°C)
- Temperatura inválida (menor a cero absoluto)

**Pistas:**
- Usa `cin` para leer entrada
- Usa `#include <iomanip>` y `setprecision()` para controlar decimales
- Usa `double` para temperaturas (pueden ser decimales)
- Valida con `if`

---

### Desafío 2: Simulador de Contador Binario

**Dificultad:** ⭐⭐⭐ (Retadora)

**Problema:**
Escribe un programa que simule un contador binario de 8 bits que cuenta desde 0 hasta 255, mostrando:
1. El número en decimal
2. El número en binario (formato: 11110000)
3. Número de bits en 1 (población de bits)

**Requisitos:**
1. El programa debe iterar desde 0 hasta 255
2. Para cada número, calcular su representación binaria
3. Contar cuántos bits son 1 (usa operadores bitwise)
4. Mostrar cada 16 números (es decir: 0, 16, 32, 48, ...)

**Salida esperada:**
```
Decimal: 0    Binario: 00000000    Bits en 1: 0
Decimal: 16   Binario: 00010000    Bits en 1: 1
Decimal: 32   Binario: 00100000    Bits en 1: 1
...
Decimal: 255  Binario: 11111111    Bits en 1: 8
```

**Desafío extra:**
- ¿Cuál es el número que tiene más bits en 1?
- Calcula cuántos números entre 0-255 tienen exactamente 4 bits en 1

**Pistas:**
- Usa bitwise AND (`&`) para extraer cada bit
- Usa bitwise shifts (`>>`) para recorrer los bits
- Para convertir a binario, trabaja bit por bit
- Usa un bucle `for` anidado si es necesario

---

### Desafío 3: Simulador Interactivo de Memoria

**Dificultad:** ⭐⭐⭐⭐ (Muy Retadora)

**Problema:**
Escribe un programa que simule memoria como un array de 8 "celdas" (bytes virtuales).

**Requisitos:**
1. El programa debe permitir:
   - `SET n valor`: Escribe `valor` en celda `n` (0-7)
   - `GET n`: Lee el valor de celda `n`
   - `PRINT`: Muestra el estado de toda la memoria
   - `EXIT`: Salir

2. Cada celda puede almacenar un número entre -128 y 127 (simula un `char`)

3. Mostrar la memoria en formato visual:
```
Estado actual de memoria:
[Celda 0]: 5    [Celda 1]: -10   [Celda 2]: 0  ...
[Celda 4]: 42   [Celda 5]: 0     [Celda 6]: 127 ...
```

4. El programa debe validar:
   - Que el número de celda esté entre 0-7
   - Que el valor esté entre -128 y 127
   - Que el comando sea válido

**Ejemplo de sesión:**
```
Comando: SET 0 42
Valor 42 escrito en celda 0.

Comando: SET 1 -15
Valor -15 escrito en celda 1.

Comando: PRINT
[Celda 0]: 42    [Celda 1]: -15   [Celda 2]: 0   [Celda 3]: 0
[Celda 4]: 0     [Celda 5]: 0     [Celda 6]: 0   [Celda 7]: 0

Comando: GET 0
Valor en celda 0: 42

Comando: EXIT
```

**Desafíos extras:**
- Implementa `SWAP n m`: Intercambia valores entre dos celdas
- Implementa `CLEAR`: Borra toda la memoria
- Implementa `SUM`: Suma todos los valores y muestra el resultado

**Pistas:**
- Usa un array `int memoria[8]` para almacenar valores
- Usa `cin` para leer comandos
- Usa `string` para comparar comandos (o convierte a números)
- Usa bucles `while` con condicionales
- Valida TODAS las entradas

---

## 📊 Checkpoint: Preguntas de Autoevaluación

Antes de pasar al siguiente módulo, responde internamente:

1. **¿Puedo explicar qué sucede en memoria cuando declaro `int x = 5;`?**
2. **¿Entiendo por qué `int` usa 4 bytes y `char` usa 1?**
3. **¿Puedo diferenciar entre `=` (asignación) y `==` (comparación)?**
4. **¿Sé cuándo usar `for` vs `while`?**
5. **¿Entiendo cómo funcionan los operadores bitwise?**

Si respondiste "no" a alguna, revisa esa sección antes de continuar.

---

## 🚀 Próximos Pasos

Después de completar los 3 desafíos, estarás listo para:
- **Módulo 2:** Funciones (parámetros por valor, stack, scope)
- **Módulo 3:** Arrays y Strings

---

**Fin del Módulo 1**

Envía tus soluciones a los desafíos y verificaremos línea por línea. 🎯
