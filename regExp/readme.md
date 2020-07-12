# Expresiones regulares

## Info:

- Curso de expresiones regulares en Platzi. [(enlace aquí)](https://platzi.com/clases/expresiones-regulares/)

## 1. Qué es y para qué sirven las expresiones regulares

- Es una secuencia de caracteres que conforma un patrón de busqueda. Se utilizan principalmente para la busqueda de patrones de cadenas de caracteres u operaciones de sustituciones.
- Sirven para optimizar tiempo y evitar busquedas generalizadas.

## 2. El caracter `.` 

- Cada espacio es ocupado por un caracter.
- El `.` denota cualquier caracter. Cabe mencionar que el 'match' ocurre por cada uno de los caracteres que se tiene en el texto.

## 3. Las clases predefinidas

- `\w` -> Encuentra todos lo que puede ser parte de una palabra.
- `\d` -> Encuentra todos los digitos.
- `\s` -> Encuentra los 'white spaces' o espacios en blanco.

## 4. Las clases construidas 

- Dada la siguiente clase: `[a-zA-Z0-9_\.]`, vease la siguiente explicación: 
    - `[]` -> Abrir una clase.
    - `[0-9]` -> Busca un rango de números.
    - `[a-z]` -> Busca un rango de letras en minuscula.
    - `[A-Z]` -> Busca un rango de letras en mayuscula.
    - `[_]` -> Busqueda personalizada para el 'guión bajo'.
    - `[\.]` -> El `\` permite 'escapar' de la clase operadora: `.`.

## 5. Los delimitadores numéricos: 

- `+` -> Encuentra uno o más. 'Si deben aparecer'.
- `*` -> Encuentra todos los caracteres del antecesor. Cero o muchos. 'Si pueden aparecer'.
- `?` -> Encuentra cero o uno.

## 6. Los contadores 

- `{1,4}` -> `1` es la cuota inicial y `4` la cuota final.

## 7. El caso de `?` como delimitador

- Permite hacer los 'matchs' más pequeños.
- Ejemplo: `.+?[,\n{1,1}]`, siendo el `?` el que nos permite tener un match más especifico de nuestra busqueda.

## 8. Not `^`, su uso y sus peligros

- Nos permite invertir o mostrar lo contrario a la clase escrita, por ejemplo en: `[^0-5a-c]`, el `^` niega toda la clase: `[0-5a-c]`.

## 9. Principio (`^`) y final de línea (`$`)

- Permite la creación de patrones unicos y condicionales de linea.- Ejemplo: `^\d{3,5}$`, solo hará el 'match' en la linea que contenga dicha busqueda.

## 10. Expresiones comunes:

  10.1 Mails

  - `[\w\._]{1,30}\+?[\w]{0,10}@[\w\.\-]{3,}\.\w{2,5}`

  10.2. Teléfonos

  - `^\+?\d{2,3}[^\da-z]?+[#pe]?\d*$`

  10.3 Logs

  - `^\[LOG.*\[LOG\].*user:@beco\] .*$`

  10.4 Locaciones

  - `^\-?\d{1,3}\.\d{1,6},\s?\-?\d{1,3}\.\d{1,6},.*$`
 
  10.5 URL s

  - `https?:\/\/[\w\-\.]+\.\w{2,5}\/?\S*`

  10.6 Nombres

  - `^[A-ZÑÁÉÍÓÚ]?[a-zñáéíóú]{3,}\s?[A-ZÑÁÉÍÓÚ]?[a-zñáéíóú]{0,}\s?[A-ZÑÁÉÍÓÚ]?[a-zñáéíóú]{0,}.*$`

## 11. Búsqueda y reemplazo

- Dado el archivo: `movies.dat`, usese la siguiente expresión regular: `^\d+::([\w\s:,\(\)'\.\-&!\/]+)\s\((\d\d\d\d)\)::.*$`

## 12. Python

- `ver regex.py`
