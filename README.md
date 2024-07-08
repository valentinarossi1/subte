# SUBTE

Subte es una pagina web para realizar pedidos online de sanguches, teniendo la posibilidad de elegir entre diferentes tipos de panes, bases, adicionales y salsas. 

### Pre-requisitos 📋

Docker, Docker postgres, sqlachemy, venv, psql, psycopg2, CORS y flask_cors


### Instrucciones 🔧


.Activo venv:
->source venv/bin/activate

.Iniciar la base de datos:
->sudo docker start subte

.Crear la base de datos(si es necesario):
-> sudo docker run --name subte -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=subte -p 5432:5432 -d postgres
Si no se puede iniciar:
->verificacion purerto -> sudo lsof -i tcp:5432
->sudo kill <PID>> 

.Conectarse al contenedor subte:
->ingresar docker -> sudo docker exec -it subte bash
->ingresar db -> psql -U postgres --password (password=postgres)
->\connect subte (password=postgres)

.Activar la base de datos:
->python3 main.py


## Autores ✒️

Valentina Rossi (valentinarossi1)
Natanael Brizuela (nbrizuela-fi)
Ana Elizondo (anitaelizondo)

---
Hecho con ❤️
