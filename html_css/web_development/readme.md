# CURSO DE DESARROLO WEB ONLINE

## 1. Introducción

- Es todo lo que concebimos dentro un navegador, como Chrome, Firefox o Internet Explorer.
- ¿Cómo funciona internet?
    - Esta compuesto por clientes, internet y servidores.
    - Servidor: Es como un computadora que 'esta prendida todo el tiempo'. Es tambien conocido como 'Hosting'.
- Profesiones dentro del desarrollo web
    - Frontend: Son los encargados de cuidar toda la aparencia y experiencia del usuario.
    - Backend: Resguardan los datos y la seguridad de las aplicaciones.
- Tecnologias de un FrontEnd
    - HTML: Lenguaje de marcado para hacer websites, como texto, imagenes, video, enlaces, etc.
    - CSS (Cascade Style Sheet): Hojas en cascada, que nos permite definir la presentación de documentos HTML.
    - JavaScript: Es el lenguaje de programación del navegador.
- ¿Cómo hacerte un buen Frontend?
    - 'El mejor desarrolador es el que mejor preparado este'.

## 2. Plan de estudios para ser un gran desarrollador web

- Git y Git Hub -> Desarrollo Web -> Responsive Design -> CSS Grid Layout -> Animaciones para la web -> PostCSS -> de JQuery a JS -> Fundamentos de JS -> WebPack -> ReactJS -> Redux -> React Router.

## 3. Software para trabajar en desarrollo web e introducción al proyecto

- Proyecto: Vamos a realizar un portafolio a modo plantilla.
- Software: Visual Studio Code.

## 4. DOM

- Document Object Model: Modelo de documentos que se carga en el navegador web y que representa el documento como un arbol de nodos.
- Como ver un website.

## 5. Etiquetas

- Cada etiqueta tiene una determinada función.
- Es usada para crear contenido.
- Sintaxis: `<nombre> contenido </nombre>`, `<p> Esto es un parrafo </p>`, `<img src="nombre.jpg"/>`.
- `Head`: Cabecera
    - `Doctype` : Que tipo de documento estamos escribiendo.
    - `hmtl` : Donde va esta envuelto nuestro codigo.
    - `title`: Sirve para poner el titulo en el tab.
    - `meta` : Que codificado estamos usando, ejemplo: UTF-8
- `Body`: Cuerpo
    - `article` : Articulo.
    - `nav` : menus de navegación.
    - `aside` : información no relevante.
    - `section` : Secciones.
    - `h1 - h6` : Tipos de titulos.

## 6. Estructura de nuestro sitio web

- ver `index.html`

## 7. Atributos HTML

- Las etiquetas o 'tags', funcionan de tal manera que un enlace, imagen o archivo pueda comportarse como tal.

## 8. Formas de agregar estilos a HTML

- Estilo en línea (Inline):
    - Utiliza el atributo style.
    - No es para nada recomendado ya que Html sirve para definir la estructura y semántica del código y no el aspecto visual, aquí estaríamos mezclando todo.

- Estilo interno (Internal):
    -Utiliza una etiqueta style.
    -Separa en cierto modo, de una forma menos sucia (por decirlo así). Esta forma sigue sin ser la más recomendada porque seguimos mezclando lo que es el aspecto visual con la estructura y semántica del código.

- Estilo externo (External):
    -Utilizando un archivo CSS externo al documento HTML.
    -Esta es la forma más recomendada porque estamos separando totalmente la estructura y semántica con el aspecto visual.

## 9. Reglas, selectores, declaraciones, propiedades y valores de CSS

![selectores](https://github.com/jamesnoria/Learning-to-Code/blob/master/html_css/web_development/imagenes/selectores.jpg)

## 10. Unidades de medida y colores
    
- Podemos representar un color de 3 formas dentro de CSS:

    -Palabra clave: red, blue, pink, etc.
    - Hexadecimales: 0123456789ABCDEF
    - hls() hlsa()

    - #000000 = Negro
    - #FFFFFF = Blanco

- Se representan por grupos de 2 -> Red, Green, Blue

    - #FF0000 = Rojo
    - #00FF00 = Verde
    - #0000FF = Azul

- Para obtener un color más exacto se utiliza rgb o rgba:

    - rgb(0, 200, 145)
    - rgba(0, 50, 70, 0.5) para obtener transparencia

- ¿Qué es un pixel?
    -La menor unidad homogenea en color que forma parte de una imagen digital.

## 11. Tipos de Background

- background-color para agregar unn color de fondo
- color para agregar un color al texto
- text-decoration para modificar la decoración del texto
- background-image para agregar una imagen de fondo
- background-size para modificar el tamaño del background asignado
- background-repeat para modificar la repetición del backgound asignado
- background-position para modificar la posición del bakground asignado