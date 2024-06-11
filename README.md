## Intelimetrica

En la carpeta de core, agregue un archivo archivo que se llame `.env` dentro de el pegue lo siguiente `DATABASE_URL=postgresql://root:123@postgres:5432/restaurants` y guarde los cambios.

Para iniciar el proyecto ejecute el siguiente comando

* `make start-container` para levantar la base de datos y el servicio de fastpi

Si se desean coectar a la base de datos, se puede hacer con las siguientes credenciales `database=restaurants`, `user=root`, `password=123`

En la url `http://localhost:8000/docs` podran ver la documentacion de la api

En la carpeta `postman` vienen las peticiones guardas y estas se pueden exportar a `postman`