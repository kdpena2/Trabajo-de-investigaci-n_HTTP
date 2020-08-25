# Trabajo-de-investigación_HTTP

****Creación de un servidor web REST y un cliente REST con Node-Red****


****PROBLEMA:****
<p>¿Qué es un servidor web  Rest y cómo implementarlo a través del uso de nodos http  en Node Red ?</p>

****OBJETIVO GENERAL:****

 <p>Identificar y describir de manera general los parámetros de configuración de los nodos http en Node-Red  y definir un  servidor y cliente web Rest para el diseño del mismo con los nodos mencionados mediante el análisis de información para su comprensión y posterior implementación.</p>

****OBJETIVOS ESPECÍFICOS:****

 <p><li>Identificar estudios recientes que contengan información acerca de los nodos http y un servidor web Rest, a fin de comprender  el objeto a investigar y las distintas aplicaciones que tiene.</li></p>
<p><li>Comprender la funcionalidad y parámetros de configuración de los nodos necesarios para el desarrollo de un servidor web Rest.</li></p>
<p><li>Desarrollar un ejemplo básico en el que se evidencie la implementación de varios nodos para el diseño de un servidor web Rest. </li></p>

****ESTADO DEL ARTE****

***API REST vinculadas: un software intermedio para la integración de API REST semántica***

<p>Diego Serrano,Eleni Stroulia, Diana Lau y Tinny Ng</p>
<p>Departamento de Computación. Sci., Univ. de Alberta, Edmonton, AB, Canadá</p>
 
 
<p>Este artículo menciona que durante los últimos años gran parte de los  servicios REST ha proporcionado una sintaxis simple que permite acceder  de manera directa a recursos de datos, sin embargo, para utilizar estos servicios, aquellos que los desarrollan deben comprender los "contratos de uso de información" mismos que se especifican en lenguaje natural para además crear aplicaciones que se beneficien de múltiples servicios existentes, deben mapear los esquemas de recursos subyacentes en el código, todo esto resulta en un  proceso difícil el cual es  propenso a errores.Por lo que en este artículo, se propone un marco conceptual para la integración de servicios REST basado en modelos de datos enlazados.En este sentido , los datos expuestos por los servicios REST se mapean a esquemas de datos enlazados, en base a estas descripciones, se ha desarrollado un middleware que puede componer automáticamente llamadas a API para responder a consultas de datos (en SPARQL). Además, se desarrolló un modelo RDF para caracterizar los protocolos de control de acceso de estas API. En la mayoría de los casos, la estructura de las respuestas de estas API siguen un formato sintáctico común,según lo dictado por el estilo REST. Sin embargo, estas respuestas típicamente no se basan en la semántica, que es un requisito necesario y  previo para interpretar e interconectar automáticamente el contenido intercambiado.Por lo que se menciona además que las aplicaciones que dependen de las API web todavía requieren un considerable esfuerzo por parte de los desarrolladores de aplicaciones. Primero necesitan obtener credenciales necesarias de los proveedores para acceder a las API,luego  tienen que escribir código para invocar a cada individuo.
Lo que implica la necesidad de comprender la naturaleza de la datos que estas API consumen y producen para componer API compatibles e integrar sus datos mapeando el diferentes esquemas implícitos,por lo que se acude a un middleware LRA para automáticamente descubrir, componer e invocar  REST API. El middleware se basa en una especificación semántica de las funcionalidades de entrada-salida de las API y sus atributos no funcionales, descritos en términos de datos vinculados.En el estudio se  ha elegido ontologías RDF Linked-Data para semánticamente anotar las API REST, debido a su amplia adopción, y su flexibilidad para expresar relaciones funcionales entre elementos en un servicio web. En consecuencia, el middleware LRA presenta un enfoque novedoso para responder consultas SPARQL a través de un proceso completamente automático. Este proceso, apoyado por el middleware LRA, implica el descubrimiento de REST API relevantes para la consulta SPARQL de entrada, la composición de estas API a través de su producción-consumo de datos , la ejecución de los planos compuestos relaciones a través de la invocación de las API y la vinculación y difusión de sus respuestas.</p>
 
<p>Fecha de la conferencia: 25-30 de junio de 2017</p>
<p>Fecha de adición a IEEE Xplore : 11 de septiembre de 2017</p>

<p>Este estudio se relaciona con la investigación realizada ya que demuestra que API nos permite interactuar con un sistema de información sin necesidad de un conocimiento de la estructura interna o de la tecnología utilizada, lo que reduce la dificultad en el desarrollo de aplicaciones ya que nos proporciona una sintaxis simple a la comprensión.Sin embargo,este estudio a diferencia del nuestro se basa en un middleware que se basa en una especificación semántica de las funcionalidades de entrada-salida de las API.Además a lo largo del trabajo se menciona la importancia del modelo REST en el diseño de aplicaciones y servicios de tipo cliente-servidor.</p>

***El diseño de un sistema web integrado basado en la arquitectura REST***

<p>Yunwei Zhao y Xin Wan</p>
<p>Universidad de Comunicación de China, Escuela de Ingeniería de la Información y la Comunicación, Beijing, China</p>
<p>Con el objetivo de abordar los problemas de alto acoplamiento, gran desperdicio de recursos y baja expansibilidad en el modo de desarrollo de sistema WEB integrado tradicional, este documento presenta un diseño de desarrollo de sistema WEB integrado basado en el estilo REST. En este artículo, los datos del sistema se resumen como un recurso. El front-end inicia una solicitud de recursos mediante la solicitud AJAX mejorada y llama a la API RESTful para realizar la transmisión de recursos, y el servidor procesa las solicitudes del cliente a través del programa CGI. La implementación de este esquema mejora la versatilidad y la capacidad de expansión del sistema WEB integrado y reduce el costo de memoria del servidor.El modo de desarrollo tradicional de la web integrado El sistema tiene un alto grado de acoplamiento entre la parte delantera y back-end. Porque el back-end también maneja las páginas del front-end además del procesamiento de datos. Entonces hay algunos problemas como alto consumo de memoria, ciclo de desarrollo largo, costes elevados por mantenimiento y bajo rendimiento de expansión. A fin de resolver estos problemas, este documento propone una red integrada esquema de diseño del sistema basado en arquitectura REST. Se abstrae datos del sistema en recursos, adopta la separación delantera y trasera estructura, de modo que el front-end solo se utilice para el negocio lógica y páginas, y el back-end solo se usa para recursos Procesando. Usando una interfaz API RESTful para transferir recursos entre el front-end y el back-end.La API RESTful es una interfaz API basada en REST arquitectura. El recurso se identifica y se ubica por URL y operado por métodos HTTP (como POST, GET, PUT,BORRAR.etc). Es fácil procesar recursos con RESTful API.Comparado con el acoplamiento de los extremos delantero y trasero esquema de desarrollo, la API RESTful enfatiza la versatilidad de la interfaz. La separación de la parte delantera y trasera La arquitectura que utiliza API RESTful tiene las ventajas de un bajo acoplamiento, baja complejidad y alta expansibilidad. Sin embargo,debido a los altos requisitos de recursos del desarrollo web basado en REST, y la limitación de CGI en HTTP protocolo, es difícil trasplantar directamente la web desarrollo en estilo REST para el sistema integrado, necesita algunos cambios.. En este artículo, nos centramos en el diseño e implementación de la interfaz RESTful API. Esta parte principalmente utiliza las funciones orientadas a recursos de REST y HTTP verbos, cambia la forma de solicitud de datos de AJAX, para mejorar la versatilidad y la capacidad de expansión de la web integrada sistemas</p>
<p>En este artículo al igual que el nuestro se centra en la importancia de la arquitectura REST en el  desarrollo web ya que se apoya totalmente en el estándar HTTP,permitiendo el manejo efectivo de los recursos que viajan desde el lado del cliente al servidor y viceversa.</p>
<p>Fecha de la conferencia: 20-22 de diciembre de 2019</p>
<p>Fecha de adición a IEEE Xplore : 13 de febrero de 2020</p>

***Estrategia de diferenciación de servicios basada en las demandas de los usuarios para servidores web Https***



****MARCO TEÓRICO****

***PROTOCOLO  HTTP***

<p>HTTP (Protocolo de Transferencia de Hipertexto), es un conjunto de reglas acordadas para transferir texto con atributos propios de Internet, que permite a dos máquinas comunicarse entre sí.</p>
<p>Se trata de un protocolo que opera a través de solicitudes entre un cliente y un servidor. Este término es utilizado para describir el lenguaje basado en texto. No importa cómo se desarrolle, el objetivo del servidor será siempre entender y devolver respuestas de texto sencillo.</p>
<p>Los clientes y servidores se comunican intercambiando mensajes individuales. Los mensajes que envía el cliente, se llaman peticiones, y los mensajes enviados por el servidor se llaman respuestas.</p>

**Arquitectura de los sistemas basados en  HTTP**

<p>Cada petición individual se envía a un servidor, el cual la gestiona y responde. Entre cada petición y respuesta, hay varios intermediarios, normalmente denominados proxies, los cuales realizan distintas funciones, como: gateways o caches. </p>


![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%201.png)


**Cliente: el agente del usuario**

<p>Cada conversación en la web comienza con una petición, la cual es enviada por el cliente que espera la respuesta.</p>
<p>Ejemplo de petición en lenguaje HTTP:</p>
<p>GET / HTTP/1.1</p>
<p>Host: google.com</p>
<p>Accept: text/html</p>
<p>User-Agent: Chrome/31.0.1650.57 (Macintosh; Intel Mac OS X 10_9_0)</p>
<p>Este mensaje comunica todo lo necesario acerca de qué recurso exactamente está solicitando el cliente.</p>
<p>La primera línea de una petición HTTP es la más importante y contiene dos cosas:</p>
<p><li>el URI (Identificador de recursos uniforme)</li></p>
<p><li>el método HTTP</li></p>
<p>El URI (e.g. /, /contact, etc) es la única dirección o ubicación que identifica el recurso que el cliente quiere.</p>
<p>El método HTTP (e.g. GET) define lo que quieres hacer con el recurso. Los métodos HTTP son los verbos de la petición y definen las pocas maneras comunes que pueden actuar sobre el recurso:</p>
<p><li>GET Recuperar el recurso del servidor</li></p>
<p><li>POST Crear un recurso en el servidor</li></p>
<p><li>PUT Actualizar el recurso en el servidor</li></p>
<p><li>DELETE Borrar el recurso del servidor</li></p>

***El servidor Web***

<p>Una vez que el servidor ha recibido la petición, sabe exactamente qué recurso necesita el cliente (vía URI) y qué es lo que el cliente quiere hacer con ese recurso (vía método HTTP).</p>
<p>Ejemplo de respuesta enviada al navegador:</p>
<p>HTTP/1.1 200 OK</p>
<p>Date: Sun, 01 Dec 2013 18:17:45 GMT</p>
<p>Server: Apache/2.2.22 (Ubuntu)</p>
<p>Content-Type: text/html</p>

<p><html></p>
      <p><!-- ... --></p>
<p></html></p>
<p>La respuesta HTTP contiene el recurso solicitado, así como otra información acerca de la respuesta. En la primera línea se encuentra el código de estado de respuesta HTTP (200 en este caso). El código de estado comunica el resultado global de la solicitud.</p> 
<p>Existen diferentes códigos de estado que indican éxito, error o que el cliente necesita hacer algo (e.g. redirigir a otra página). Los códigos de estado más comunes son:</p>
<p><li>200 OK. Indica éxito.</li></p>
<p><li>304 Not Modified. Esto muestra que el recurso en cuestión no ha cambiado y que el navegador debe cargarlo desde su caché.</li></p>
<p><li>404 Not Found. Esto sugiere que el recurso no se encuentra en el servidor.</li></p>

<p><li>401 Authorization Required. Esto indica que el recurso está protegido y requiere credenciales válidos antes de que el servidor pueda conceder el acceso.</li></p>
<p><li>500 Internal Error. Esto significa que el servidor ha tenido un problema procesando la petición.</li></p>

<p>Al igual que la petición, una respuesta HTTP contiene piezas de información adicionales conocidas como cabeceras HTTP o headers. El cuerpo o body de un mismo recurso puede ser devuelto en múltiples formatos diferentes como HTML, XML o JSON.</p>

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%202.png)



***SERVIDOR WEB REST***

<p>REST (Transferencia de Estado Representacional) se trata de un estilo de arquitectura de software que se utiliza para describir cualquier interfaz entre diferentes sistemas que utilicen HTTP para comunicarse. Éste cambió por completo la ingeniería de software a partir del 2000. Se trata de un nuevo enfoque de desarrollo de proyectos y servicios web que fue definido por Roy Fielding. </p>
<p>Dicho estilo arquitectónico se caracteriza por seguir los siguientes principios:</p>
<p><li>Cliente-servidor: las aplicaciones REST tienen un servidor que administra los datos y el estado de la aplicación. El servidor se comunica con un cliente que maneja las interacciones del usuario. </li></p>
<p><li>Sin estado: los servidores no mantienen ningún estado de cliente. Los clientes gestionan el estado de su aplicación. Sus solicitudes a los servidores contienen toda la información necesaria para procesarlas.</li></p>
<p><li>En caché: los servidores deben marcar sus respuestas como almacenables en caché o no. Por lo tanto, las infraestructuras y los clientes pueden almacenarse en caché cuando sea posible para mejorar el rendimiento. Pueden deshacerse de información que no se puede almacenar en caché, por lo que ningún cliente utiliza datos obsoletos.</li></p>
<p><li>Interfaz uniforme: esta es la característica central que distingue el estilo arquitectónico REST de otros estilos basados ​​en red. Los servicios REST proporcionan datos como recursos, con un espacio de nombres coherente.</li></p> 
<p><li>Sistema en capas: los componentes del sistema no pueden "ver" más allá de su capa. Por lo tanto, puede agregar fácilmente equilibradores de carga y proxies para mejorar la seguridad o el rendimiento.</li></p>
<p><li>Las operaciones más importantes relacionadas con los datos en cualquier sistema REST y la especificación HTTP son Get, Post, Put, Delete. </li></p>

***Recursos REST***

<p>Un recurso REST es cualquier cosa que sea direccionable (y por lo tanto, accesible) a través de la Web. Por direccionable nos referimos a recursos que puedan ser accedidos y transferidos entre clientes y servidores. Por lo tanto, un recurso es una correspondencia lógica y temporal con un concepto en el dominio del problema para el cual se implementa una solución.</p>

***API REST***

<p>Una API REST es al día de hoy, lo más usado en el desarrollo de servicios de aplicaciones, tanto que en la actualidad no existe proyecto o aplicación que no la disponga en la creación de servicios profesionales. Esto es así porque REST es el estándar más lógico, eficiente y habitual en la creación de APIs para servicios de Internet. </p>
<p>Es una interfaz para conectar varios sistemas basados en el protocolo HTTP, el cual  sirve para obtener y generar datos y operaciones sobre esos mismos datos en formatos muy específicos, como XML y JSON, siendo el segundo el más usado en la actualidad ya que es más ligero y legible en comparación al formato XML. </p>

***Ventajas de una API REST***

<p><li>Separación entre el cliente y el servidor. El protocolo REST separa totalmente la interfaz de usuario del servidor y el almacenamiento de datos. </li></p>
<p><li>Visibilidad, fiabilidad y escalabilidad. Con la separación entre cliente y servidor, cualquier equipo de desarrollo puede escalar el producto sin excesivos problemas. Se puede migrar a otros servidores o realizar todo tipo de cambios en la base de datos, siempre y cuando los datos de cada una de las peticiones se envíen de forma correcta. Además esta separación facilita tener en servidores distintos el front y el back y eso convierte a las aplicaciones en productos más flexibles a la hora de trabajar.</li></p>
<p><li>La API REST siempre es independiente del tipo de plataformas o lenguajes. La API REST siempre se adapta al tipo de sintaxis o plataformas con las que se estén trabajando, lo que ofrece una gran libertad a la hora de cambiar o probar nuevos entornos dentro del desarrollo. Con una API REST se pueden tener servidores PHP, Java, Python o Node.js.</li></p>
<p><li>Todos los objetos se manipulan mediante URI. Por ejemplo, si tenemos un recurso usuario y queremos acceder a un usuario en concreto nuestra URI sería /user/identificadordelobjeto, con eso ya tendríamos un servicio USER preparado para obtener la información de un usuario, dado un ID.</li></p>
<p><li>Existe la posibilidad de hacer la API pública, permitiendo dar visibilidad.</li></p>



***NODOS NECESARIOS PARA LA CREACIÓN DE UN SERVIDOR WEB REST ***
 
***Nodo http***

<p>Para utilizar el servidor y el cliente HTTP, es necesario require('http').
Las interfaces HTTP en Node.js están diseñadas para admitir muchas características del protocolo que tradicionalmente han sido difíciles de usar. En particular, mensajes grandes, posiblemente codificados por fragmentos. La interfaz tiene cuidado de nunca almacenar en búfer solicitudes o respuestas completas, de modo que el usuario pueda transmitir datos.</p>

<p>Hay tres nodos http principales .</p>
<p><li>http-in: se utiliza para configurar un servidor web</li></p>
<p><li>Respuesta http : se usa con http-in para enviar respuestas.</li></p>
<p><li>Solicitud http : se utiliza para realizar solicitudes http, es decir, un cliente http.</li></p>
<p>El  nodo de solicitud http se puede utilizar para.</p>
<p><li>Recuperar páginas web de un sitio web</li></p>
<p><li>Realización de una solicitud de API.</li></p>
<p><li>Enviar y recibir datos JSON a un sitio web o API.</li></p>
<p><li>etc</li></p>
<p>El nodo enviará una solicitud y recibirá la respuesta .</p>
<p>El nodo maneja tanto la solicitud como la respuesta.</p>
 
***Nodo http in y http response***
 
<p>El HTTP In  y el HTTP Response par de nodos son el punto de partida para todos los extremos HTTP que se crean.
Cualquier flujo que comience con un HTTP In nodo debe tener una ruta a un HTTP Response nodo, de lo contrario, las solicitudes finalmente se agotarán.
El HTTP Response nodo utiliza la payload propiedad de los mensajes que recibe como cuerpo de la respuesta. Se pueden usar otras propiedades para personalizar aún más la respuesta; se tratan en otras recetas.
El Template nodo proporciona una forma conveniente de incrustar un cuerpo de contenido en un flujo. Puede ser deseable mantener dicho contenido estático fuera del flujo.
Si ha activado la autenticación http, es posible que deba agregar su ID de usuario y contraseña al comando curl. p.ej</p>

***Configuración del nodo http in***

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%203.png)


<p>El nodo admite los métodos GET, POST, PUT, DELETE y PATCH.GET es el tipo de solicitud más utilizado y era el único tipo de solicitud en la especificación HTTP original.
El nodo http-in aceptará una solicitud de obtención en la URL / servidor web ,todas las demás solicitudes serán ignoradas.</p>
<p>Si se empieza  a usar el flujo simple que se muestra a continuación, se pasa la salida del nodo http-in a un nodo de depuración y se lo puede probar  usando un navegador web.</p>


![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%204.png)


<p>Para una solicitud GET, contiene un objeto de cualquier parámetro de cadena de consulta. De lo contrario, contiene el cuerpo de la solicitud HTTP.
Un objeto de solicitud HTTP. Este objeto contiene varias propiedades que proporcionan información sobre la solicitud.</p>
<p><li>body: el cuerpo de la solicitud entrante. El formato dependerá de la solicitud.</li></p>
<p><li>encabezados: un objeto que contiene los encabezados de solicitud HTTP.</li></p>
<p><li>consulta: un objeto que contiene cualquier parámetro de cadena de consulta.</li></p>
<p><li>Parámetros: un objeto que contiene cualquier parámetro de ruta.</li></p>
<p><li>cookies: un objeto que contiene las cookies para la solicitud.</li></p>
<p><li>archivos: si está habilitado dentro del nodo, un objeto que contiene los archivos cargados como parte de una solicitud POST.</li></p>
 
***Configuración del nodo http response***


![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%205.png)


<p>Los mensajes en este nodo deben originarse en un nodo de entrada http.
Puede establecer el código de respuesta y otros encabezados de mensaje en este nodo o en un nodo anterior.</p>
<p>Las entradas en el nodo además del objeto res desde el nodo http-in son:</p>
<p><li>carga útil</li></p>
<p><li>código de estado</li></p>
<p><li>encabezados</li></p>
<p><li>galletas</li></p>
 
<p><li>Payload-string
El cuerpo de la respuesta.</li></p>
<p><li>StatusCode-number
Si se establece, se utiliza como código de estado de respuesta. Predeterminado: 200.</li></p>
<p><li>Objeto-encabezados
Si se establece, proporciona encabezados HTTP para incluir en la respuesta.</li></p>
<p><li>Objeto de cookies
Si está configurado, se puede utilizar para configurar o eliminar cookies.</li></p>
 
 
***Configuración del nodo de solicitud HTTP***

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%206.png)

<p>La configuración incluye</p>
<p>1.El método de solicitud: el nodo admite los métodos GET, POST, PUT y DELETE.
El método principal es GET, que se utiliza para obtener una página web.</p>
<p>2. La URL del recurso.</p>
<p>3. Autenticación: si el sitio web requiere autenticación, aquí se puede realizar la autenticación básica.</p>
<p>4. SSL : casilla de verificación para forzar la conexión a utilizar SSL</p>
<p>5. Respuesta: la respuesta del servidor puede ser una :</p>
<p><li>Cadena UTF-8, es decir, una página web estándar</li></p>
<p><li>Un búfer binario : datos binarios</li></p>
<p><li>Un objeto JSON analizado : generalmente se usa con API web. El nodo convertirá los datos JSON en un objeto JavaScript.</li></p>
 
 
![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%207.png)



 ***Nodos websocket***
 
![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%208.png)


<p>Los websockets son otra capacidad de comunicación útil que está integrada en Node-RED a través del nodo websocket. Los Websockets proporcionan una conexión TCP dúplex y fueron diseñados para permitir que los navegadores web y los servidores mantengan un 'canal de retorno' que podría usarse para aumentar el HTTP tradicional.interacciones, lo que permite a los servidores actualizar las páginas web sin que el cliente realice una nueva solicitud de extracción.</p>
<p>El nodo websocket viene en dos versiones, entrada y salida, lo que le permite escuchar los datos entrantes (entrada) o enviar (salida) en un websocket. La versión de salida está diseñada para verificar si la carga útil de salida se originó en un websocket en un nodo, en cuyo caso responde al remitente original. De lo contrario, transmitirá la carga útil a todos los websockets conectados.Además, los nodos websocket de entrada y salida se pueden configurar como servidor o cliente: en el modo de servidor 'escuchan' una URL y en el modo de cliente se conectan a una dirección IP específica.</p>

***Websocket in***

<p>De forma predeterminada, los datos recibidos de WebSocket estarán en msg.payload. El socket se puede configurar para esperar una cadena JSON correctamente formada, en cuyo caso analizará el JSON y enviará el objeto resultante como el mensaje completo.</p>


![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%209.png)



<p><li>El tipo de websocket definido por defecto (“Listen on”) es correcto, por lo que no es necesario cambiarlo. Lo que sí debemos definir es la ruta (path en inglés) en la que estará escuchando nuestro websocket.</li></p>
<p><li>Esto nos abre una nueva ventana en la que podemos definir la ruta en la que estará escuchando nuestro WebSocket. Por defecto vemos que la ruta usada es /ws/example.</li></p> 
<p><li>En el último campo se debe poner un nombre a este nodo para facilitar la lectura del flujo.</li></p>


***Websocket out***

<p>Si el mensaje que llega a este nodo comenzó en un nodo WebSocket In, el mensaje se enviará de vuelta al cliente que desencadenó el flujo. De lo contrario, el mensaje se transmitirá a todos los clientes conectados.</p>

***Configuración***

<p>Este websocket también se necesita configurar. Utilizando el mismo procedimiento que se usa para el websocket de entrada, en el que se modificarán los datos como en la imágen de muestra:</p>


![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2010.png)


<p>En este caso la configuración será más sencilla, ya que se reutiliza la misma ruta usada para el websocket de entrada. Esto es normal, dado que en realidad se está hablando de un solo WebSocket, el cual se va a usar tanto para recibir mensajes como para mandar la contestación al browser. Elija un nombre para este nodo (yo decidí llamarlo “outputsocket”).</p> 

****DIAGRAMAS****

***Diagrama de caso uso “comunicación cliente servidor”***

<p>En primer lugar el cliente solicita recepción de información al servidor este una vez comprueba el host proveniente la envía hacia el servidor para que este pueda procesarla si el host no es el mismo generado por el nodo http el servidor no reconocerá el intento de recepción de información y rechazara la llegada de datos</p>

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2011.png)


***Diagrama de codificación por bloques “metodos POST y GET”***

<p>Para la implementación de los diferentes de una web rest en node red se utiliza un nodo http in en el cual podremos el método a usar para el primer caso usamos un método post conectado a un nodo debug que nos permita observar los cambios en consola a la par se conecta este nodo con dos nodos más fuction y un nodo http response respectivamente este último nos permite visualizar la información que nuestro cliente requiera enviar en forma de objetos  {clase:objeto} en nuestro nodo fuction nos permitiremos cambiar la forma de visualizar la información eliminando los puntos intermedios y las llaves resultando de esta manera: ( objeto ) conectamos este nodo fuction a 2 salidas de información por dashboard un chart y un text en los cuales podremos visualizar lo enviado por el cliente sean palabras o sean números, la misma estructura maneja el nodo http con un método GET</p>


![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2012.png)





****LISTA DE COMPONENTES****

<p>Estos son los recursos que se han utilizado a lo largo del desarrollo del trabajo de investigación.</p>

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2013.png)


****MAPA DE VARIABLES****
 
Variables usadas:
name: 
Esta variable me permite almacenar un espacio de memoria en donde el cliente puede ingresar mediante un inut información que se vaya a enviar al servidor 
msg.payload.name:
Esta variable me permite reemplazar la visualización de objetos a una forma más amigable de {name:objeto} a simplemente el objeto impuesto por el cliente 

 ****EXPLICACIÓN DE CÓDIGO FUENTE****
 
 <p>Para la utilización del nodo http recurrimos a una estructura html en donde usaremos la etiqueta form para poder enrutar el host a nuestro servidor dentro de la etiqueta form implementamos un action que nos dirija al localhost generado por defecto por node red incluyendo el nombre atribuido en nuestra configuración del nodo en nuestro caso es test consecuente a esto generamos entradas de texto que nos permitan enviar información al lugar enrutado es decir a nuestro servidor.</p>
 
 ![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2014.png)
 
 <p>El resultando de esta codificación lo podemos ver a continuación, cada clase Name, Email and Message retendrá un distinto objeto el cual lo proporciona el cliente </p>

 
 ![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2015.png)
 
****DESCRIPCIÓN DE PRERREQUISITOS Y CONFIGURACIÓN****


 ![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2016.png)



 
****APORTACIONES****

<p>Para el desarrollo de este trabajo se ha usado XAMPP  el cual es un paquete de software libre, que consiste principalmente en el sistema de gestión de bases de datos MySQL, el servidor web Apache y los intérpretes para lenguajes de script PHP y Perl.</p>
<p>Apache: el servidor web de código abierto es la aplicación más usada globalmente para la entrega de contenidos web. Las aplicaciones del servidor son ofrecidas como software libre por la Apache Software Foundation.</p>
<p>MySQL/MariaDB: XAMPP cuenta con uno de los sistemas relacionales de gestión de bases de datos más populares del mundo. En combinación con el servidor web Apache y el lenguaje PHP, MySQL sirve para el almacenamiento de datos para servicios web. En las versiones actuales de XAMPP esta base de datos se ha sustituido por MariaDB.</p>
<p>PHP: es un lenguaje de programación de código de lado del servidor que permite crear páginas web o aplicaciones dinámicas. Es independiente de plataforma y soporta varios sistemas de bases de datos.
<p>Perl: este lenguaje de programación se usa en la administración del sistema, en el desarrollo web y en la programación de red. También permite programar aplicaciones web dinámicas.</p>
<p>Este software además  se constituye como  una herramienta de desarrollo que te permite probar tu trabajo (páginas web o programación, por ejemplo) en tu propio ordenador sin necesidad de tener acceso a internet.</p>
 
****CONCLUSIONES****

<p>El protocolo HTTP es amplio y fácil de usar. Su estructura cliente-servidor, junto con la capacidad para usar cabeceras, le permite evolucionar con las nuevas y futuras aplicaciones en Internet.</p>
<p>La principal ventaja del uso de una API REST reside en la independencia que proporciona frente a cualquier consumidor, sin importar el lenguaje o plataforma con el que se acceda a ella. Esto permite que una misma API REST sea consumida por varios clientes y que el cambio a cualquier otro tipo de consumidor no provoque impacto alguno en ella. </p>
<p>La separación entre el cliente y el servidor hace que se pueda migrar a otros servidores o bases de datos de manera transparente, siempre y cuando los datos se sigan enviado de manera correcta. APIs REST es una de las arquitecturas web más utilizadas actualmente por la flexibilidad que aporta a cualquier entorno de trabajo sea cual sea su naturaleza.</p>

****RECOMENDACIONES****

<p>Al realizar operaciones que modifican el estado de un objeto, se debe utilizar preferentemente los métodos POST, PUT y DELETE. El método GET se usa para retornar solamente una versión de lectura del recurso.</p>
<p>Se deben asegurar las apis que se desarrollen, ya que cuando se trata de aplicaciones web es muy sencillo visualizar lo que está detrás del código. </p>

****CRONOGRAMA****

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2017.png)

****BIBLIOGRAFÍA:****
[1] D. Serrano, E. Stroulia, D. Lau y T. Ng, "API de REST vinculadas: un software intermedio para la integración de API de REST semántica", 2017 IEEE International Conference on Web Services (ICWS) , Honolulu, HI, 2017, págs. 138 -145, doi: 10.1109 / ICWS.2017.26.
 
[2] Y. Zhao y X. Wan, "The Design of Embedded Web System based on REST Architecture", IEEE IV Conferencia de control de automatización, electrónica y tecnología de la información avanzada (IAEAC) de 2019 , Chengdu, China, 2019, págs. 99-103, doi : 10.1109 / IAEAC47372.2019.8997929.
 
[3] BBVAOpen4U. (23 de Marzo de 2016). API REST: qué es y cuáles son sus ventajas en el desarrollo de proyectos. Obtenido de https://bbvaopen4u.com/es/actualidad/api-rest-que-es-y-cuales-son-sus-ventajas-en-el-desarrollo-de-proyectos
 
[4] Innovation & Entrepreneurship Business School. (2019). Qué es Api Rest y por qué debes de integrarla en tu negocio. Obtenido de https://www.iebschool.com/blog/que-es-api-rest-integrar-negocio-business-tech/
 
[5] Mozilla and individual contributors. (7 de Agosto de 2020). Generalidades del protocolo HTTP. Obtenido de https://developer.mozilla.org/es/docs/Web/HTTP/Overview
 
[6] Lea, V. A. P. B. R. (2018, 22 noviembre). Node-RED: Lecture 3 – Example 3.7 Using Websockets with Node-RED – Node RED Programming Guide. Using Websockets with Node-RED. http://noderedguide.com/node-red-lecture-3-example-3-7-using-websockets-with-node-red/
 
[7] Set up websocket communication using Node-RED between a Jupyter notebook on IBM Watson Studio and a web interface. (2017). IBM Developer. https://developer.ibm.com/technologies/analytics/tutorials/setup-websockets-using-nodered/#:%7E:text=The%20websocket%20node%20in%20Node,(output)%20on%20a%20websocket.
[8] How do I use WebSockets in Node-RED to control IO on a BB-400? - Brainboxes - Industrial Ethernet IO and Serial. (2020). Brainboxes. http://www.brainboxes.com/faq/items/websockets-in-node-red-control-io-bb-400
[9] Desarrollo de una aplicación web usando Node-RED. (2019). IBM Developer. https://developer.ibm.com/es/articles/desarrollo-de-una-aplicacion-web-usando-node-red/

****ANEXOS****

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2018.png)

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2019.png)

![](https://github.com/kdpena2/Trabajo-de-investigaci-n_HTTP/blob/master/IMG/Imagen%2020.png)





