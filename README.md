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
*****imagen*****

**Cliente: el agente del usuario**

<p>Cada conversación en la web comienza con una petición, la cual es enviada por el cliente que espera la respuesta.</p>
<p>Ejemplo de petición en lenguaje HTTP:</p>
<p>GET / HTTP/1.1</p>
<p>Host: google.com</p>
<p>Accept: text/html</p>
<p>User-Agent: Chrome/31.0.1650.57 (Macintosh; Intel Mac OS X 10_9_0)</p>
<p>Este mensaje comunica todo lo necesario acerca de qué recurso exactamente está solicitando el cliente.</p>
