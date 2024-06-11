## Intelimetrica

En la carpeta de core, agregue un archivo archivo que se llame `.env`, dentro de el pegue lo siguiente `DATABASE_URL=postgresql://root:123@postgres:5432/restaurants` y guarde los cambios.

Para iniciar el proyecto ejecute el siguiente comando

*  `make start-container` para levantar la base de datos y el servicio de FastAPI

  El comando anterior levantara dos contenedores:

| Nombre | Puerto | Funcion |
|--|--|--|
| Postgres-1 | 5432 | Contiene una imagen con una base de datos de postres junto con postgis |
| Fastapi-1 | 8080 | Contiene una imagen con la api de FastAPI |


Si se desean conectarse a la base de datos, se puede hacer con las siguientes credenciales `database=restaurants`, `user=root`, `password=123`

En la url del navegador de su preferencia coloque lo siguiente `http://localhost:8000/docs` podrán ver la documentación de la API

En la carpeta `postman` vienen las peticiones guardas y estas se pueden exportar a `postman`