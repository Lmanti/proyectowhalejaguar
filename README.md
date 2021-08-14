# Proyecto Whale & Jaguar

## overview

Este proyecto consiste en la creación de una aplicación que mediante una API creada desde 0 tambien, valida tarjetas de credito mediante el [algoritmo de Luhn](https://es.wikipedia.org/wiki/Algoritmo_de_Luhn#:~:text=El%20algoritmo%20de%20Luhn%20o,cr%C3%A9dito%2C%20n%C3%BAmeros%20IMEI%2C%20etc.) e dentifica a que franquicia pertenece. También como requisito tenía que empaquetar la app en contenedores de Docker.

Para el desarrollo de la API se utilizaron las siguientes herramientas:

### Lenguaje 
- Python

### Frameworks y librerías
- Django
- Django Rest Framework
- Django Cors-Headers

Y para el desarrollo del front se utilizaron las siguientes:

### Lenguaje
- JavaScript

### Frameworks y librerías
- React

### Otras técnologias
- Docker
- Docker Compose

Para el empaquetado de la app se utilizó Docker, creando 1 archivo *Dockerfile* tanto para back, como para front, luego en la carpeta raíz se creó un fichero *docker-compose* para correr los 2 contenedores simultaneamente.

*App created by Luis Herrera*