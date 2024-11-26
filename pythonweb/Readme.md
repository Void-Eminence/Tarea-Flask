# Flask Web Interface


## Contenido
web-interface: Sitio web básico hecho con Flask y Python3.

## Instalación

### Debian

En una VM con debian fresco y recien instalado, es posible realizar la instalación del servidor web utilizando el script el script `Setup.sh` con privilegios de root. 

#### Probar el servicio

Una vez instalado los requerimientos mediante `Setup.sh`, se puede iniciar el servicio web en modo de prueba mediante `debug.sh`. Este script por defecto sube el servicio para ser accedido solamente por la maquina local (localhost/127.0.0.1) en un puerto al azar. Edite el archivo para cambiar esta configuración manualmente. Este modo de operación es solo de pruebas y no debe ser utilizado para subir un servicio a la Internet.

#### Configurar como servicio Automático

Para configurar el sitio como servicio automático se provee un script configuración de muestra `WebService.sh`. Este considera que el repo se encuentra clonado en el directorio `/srv` del sistema y que tiene los requerimientos instalados con `Setup.sh`. Es posible combinar ambos scripts para configurar el sistema en un sólo paso. Deberá editarlo para poder satisfacer las necesidades de su configuración particular.

### Docker

El sitio también incluye un archivo `Dockerfile` que permite crear un contenedor listo con el sitio web de prueba. De igual manera el archivo `Dockerfile` es provisto a manera de ejemplo para ser modificado en un desarrollo.

#### Crear contenedor

Para crear el contenedor se debe ejecutar el siguiente comando en el directorio donde se encuentra el archivo `Dockerfile`:

`docker build . -t micontenedor`

Donde `micontenedor` representa una etiqueta que se le dará al contenedor dentro de tu instancia de docker.

#### Ejecutar contenedor

El servidor web por defecto funciona en el puerto 8000, por lo que es necesario exportar lo al iniciar el contenedor. Una vez creado el contenedor, se puede correr utilizando:

`docker run -p 8000:8000 micontenedor`


## Licencia
El proyecto tiene licencia Affero GPL3 para fines educacionales. 
