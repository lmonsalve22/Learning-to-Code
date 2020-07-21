# FUNDAMENTOS DE INGENERIA DE SOFTWARE

## 1. Qué son Bits y Bytes

- La electrecidad funciona con ondas que al ser moduladas pueden producir sonido, imagenes y texto.
- Con el tiempo, las ondas electromagneticas empezaron a clasificarse por 'subidas y bajadas'(onda digital). Subida: 1 | Bajada: 0
- Bit: 1 0
- (1956, IBM) Byte: equivalente 8 bits, donde el numero anterior multiplica al siguiente: `1, 2, 4, 8, 16, 32, 64, 128`
- Se le asigna a cada posición del número binario un valor en particular, siendo 0=nada y 1=cálculo mátematico.
- Con el tiempo se asigna un byte a cada letra, conocida actualmente como la tabla 'ASCII'. Esto último genera el nacimiento de ASSEMBLER que son bytes especiales de instrucciones del procesador.
- Un byte < 256
- Con la globalización y el acceso a las computadoras por parte de muchas personas, se crean los 'UTF' que permite que todos podamos usar la tabla ASCII. Ejemplos: UTF-8, UTF-16.
- El grupo de personas que 'cuidan' la normativa de los UTF se llaman UNICODE.

## 2. Cómo funcionan los circuitos electronicos

- Los circuitos electronicos son la base de nuestra tecnologia moderna.
- Se crean en plantas de energia y se almacenan en baterias o cables directos hacia nuestras casas.
- Fujo constante de electrones que se miden en voltaje y amperaje, siendo el voltio la fuerza que mueve la electricidad por un cable del positivo al negativo(pozo a tierra o ground)

## 3. Procesadores y arquitecturas de CPU

- CPU: Ghz(velocidad del procesador), Mgz o cores(numeros de cpu que tiene nuestro computador). El material de la cual son fabricados son: Silicio. Unidad central de proceso. 
- BIOS: Chip especial instalado en las tarjetas madre de los computadores. Trata de detectar donde estan todas las cosas que estan conectadas al computador.
- Disco Duro: Es donde esta el sistema operativo (OS) y es ahí donde corren todos los programas. Con el tiempo se crean los SSD (Discos de estado solido)
- RAM: Random access memory, es una memoria volatil que solamente funciona cuando hay electricidad.
- Periféricos: Todas las cosas externas con las cuales interactuamos fuera del computador, como: Pantalla, teclado, mouse y estos usan drivers que son piezas de software que entienden como convertir las señales electricas en bits y bytes.
- GPU: Unidad de proceso grafico, sirve para la pantalla.

## 4. Que es un system on a chip

- Es una combinación de los diferentes componentes que hacen a un computador real.

## 5. Qué es la memoria RAM y cómo funcionan los discos duros

- Un disco duro tiene una memoria persistente, quiere decir que no importa si desconectamos el aparato igual seguirá prendido.
- Los archivos son secuenciales y estructurados, guardados en sistemas de archivos. ejemplo: `FAT` `NTFS`
- Los discos duros tienen algo llamado 'cabecera' o indice de archivos, estos le indican como darle una orden al procesador para encontrar el archivo.
- Las CPU tienen una mermoria llamada 'cache', que es donde se guardan las funciones más fundamentales del ordenador.
- La memoria RAM es una memoria de acceso aleatorio, ya que es ahi donde se guardan muchas cosas.
- Entre la CPU y la RAM hay un indice compartido, que permite saber donde esta el archivo que deseamos para poder correrlo en la PC.

## 6. GPUs, tarjetas de video y sonido

- Teniendo un archivo, como ejemplo, `hola.txt` y queriendo ver su contenido en pantalla. La CPU se conecta con la GPU de manera integrada, donde la GPU contiene Cores y VRam, donde de esta manera proyecta la imagen en el monitor a traves de pixeles.

## 7. Periféricos y sistemas de entrada de información

- Los sistemas operativos tienen un kernel o nucleo que es lo primero que carga la memoria RAM cuando encendemos nuestro sistema operativo.
- Luego, se cargan los drivers.
- Se continua con drivers de arranque.
- Por ultimo, esta la capa donde cargan las aplicaciones ya que ellas no deberían poder entrar a las cosas internas de nuestro navegador.
- Existe un permiso llamado `secure enclave` que es una manera de encriptar datos personales.

## 8. Arquitectura de la computación

- Tarjetas perforadas -> Cintas Magnéticas -> Disquetes de 5’25" -> Disquetes de 3’5" -> CD -> Discos Flash (usb) -> Discos duros portátiles -> Almacenamiento Cloud

## 9. Introducción a las redes, protocolos e Internet

- Switch: Conmutador (*switch*) es el dispositivo digital lógico de interconexión de equipos que opera en la capa de enlace de datos del modelo OSI. Su función es interconectar dos o más segmentos de red, de manera similar a los puentes de red, pasando datos de un segmento a otro de acuerdo con la dirección MAC de destino de las tramas en la red y eliminando la conexión una vez finalizada ésta.

- Router: Un *router* —también conocido como enrutador,12 o rúter3— es un dispositivo que proporciona conectividad a nivel de red o nivel tres en el modelo OSI. Su función principal consiste en enviar o encaminar paquetes de datos de una red a otra, es decir, interconectar subredes, entendiendo por subred un conjunto de máquinas IP que se pueden comunicar sin la intervención de un encaminador (mediante puentes de red o un switch), y que por tanto tienen prefijos de red distintos. Estos puedo o no tener WIFI.

- IP list: Dirección IP (Internet Protocol) es una matrícula identificativa que te define dentro de una red, ya sea esta interna o externa, de cara a Internet. Y una IP list no de ja de ser una lista donde se guarda IPs en un router.

- DHCP: DHCP (siglas en inglés de Dynamic Host Configuration Protocol, en español «protocolo de configuración dinámica de host») es un servidor que usa protocolo de red de tipo cliente/servidor en el que generalmente un servidor posee una lista de direcciones IP dinámicas y las va asignando a los clientes conforme éstas van quedando libres, sabiendo en todo momento quién ha estado en posesión de esa IP, cuánto tiempo la ha tenido y a quién se la ha asignado después. Así los clientes de una red IP pueden conseguir sus parámetros de configuración automáticamente.

- MAC Address: La dirección MAC (siglas en inglés de Media Access Control) es un identificador de 48 bits (6 bloques de dos caracteres hexadecimales (4 bits)) que corresponde de forma única a una tarjeta o dispositivo de red. Se la conoce también como dirección física, y es única para cada dispositivo. Está determinada y configurada por el IEEE(los últimos 24 bits) y el fabricante (primeros 24 bits) utilizando el organizationally unique identifier. La mayoría de los protocolos que trabajan en la capa 2 del modelo OSI usan una de las tres numeraciones manejadas por el IEEE: MAC-48, EUI-48, y EUI-64, las cuales han sido diseñadas para ser identificadores globalmente únicos. No todos los protocolos de comunicación usan direcciones MAC, y no todos los protocolos requieren identificadores globalmente únicos.

- Modem: Un módem (del inglésmodem, acrónimo de *modulator demodulator*; pl.módems)1 es un dispositivo que convierte las señales digitales en analógicas(modulación) y viceversa (desmodulación), y permite así la comunicación entre computadoras a través de la línea telefónica o del cablemódem. Sirve para enviar la señal moduladora mediante otra señal llamada portadora.

## 10. Puertos y protocolos de red 

- Los routers son las puertas de enlaces a diferentes redes.
- IP: `127.0.0.1` : localhost o siempre apuntas a uno mismo.
- IPLAN: Local Area Network, `192.168.0.20`, donde los primeros tres números se mantienen igual y el resto lo guarda.


## 11. Qué es una dirección IP y el protocolo de Internet

## 12. Cables submarinos, antenas y satelites en Internet

## 13. Qué es un dominio, DNS o Domain Name System

## 14. Cómo los ISP hacen Quality of Service o QoS

## 15. Cómo funciona la velocidad en Internet

## 16. Qué es el Modelo Cliente/Servidor

## 17. Cómo funciona realmente un sitio web

## 18. Internet es más grande de lo que crees

## 19. Diferencias entre Windows, Linux, Mac, iOS y Android

## 20. Permisos, niveles de procesos y privilegios de ejecución

## 21. Fundamentos de sistemas operativos móviles

## 22. Sistemas operativos embebidos e Internet of Things

## 23. Cómo funciona .zip: Árboles binarios

## 24. Metadatos, cabeceras y extensiones de archivos

## 25. Cómo funciona el formato JPG

## 26. Videos, contenedores, codecs y protocolos
