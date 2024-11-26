#!/bin/bash

#HOST='0.0.0.0' # Permite la conexión remota
HOST='127.0.0.1' #Permite solo conexiones locales

#PORT='6000' # Por defecto elige un puerto al azar. 

python3 web-interface/debug.py $HOST $PORT
