1. Qué es y para qué sirven las expresiones regulares

- Es una secuencia de caracteres que conforma un patrón de busqueda. Se utilizan principalmente para la busqueda de patrones de cadenas de caracteres u operaciones de sustituciones.
- Sirven para optimizar tiempo y evitar busquedas generalizadas.

2. El caracter `.` 

- Cada espacio es ocupado por un caracter.
- El `.` denota cualquier caracter. Cabe mencionar que el 'match' ocurre por cada uno de los caracteres que se tiene en el texto.

3. Las clases predefinidas

- `\w` -> Encuentra todos lo que puede ser parte de una palabra.
- `\d` -> Encuentra todos los digitos.
- `\s` -> Encuentra los 'white spaces' o espacios en blanco.

4. Las clases construidas 

- Dada la siguiente clase: `[a-zA-Z0-9_\.]`, vease la siguiente explicación: 
    - `[]` -> Abrir una clase.
    - `[0-9]` -> Busca un rango de números.
    - `[a-z]` -> Busca un rango de letras en minuscula.
    - `[A-Z]` -> Busca un rango de letras en mayuscula.
    - `[_]` -> Busqueda personalizada para el 'guión bajo'.
    - `[\.]` -> El `\` permite 'escapar' de la clase operadora: `.`.

3. Los delimitadores numéricos: `+`, `*`, `?`
1. Los contadores `{1,4}`

1. Not `^`, su uso y sus peligros

1. El caso de `?` como delimitador

1. Principio (`$`) y final de línea (`^`)

1. Expresiones comunes:
  1. mails
  1. teléfonos
  1. logs
  1. nombres
  1. locaciones
    1. [what three words](https://what3words.com/)

1. Búsqueda y reemplazo

1. Procesadores de texto

1. `grep` y `find` desde consola

1. Regex en

  1. PHP
  1. Javascript
  1. Python
  1. Perl (aunque se burlen)
