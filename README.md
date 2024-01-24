# Introducción
Esta API está enfocada en la asignación de citas de clientes a peluqueros

# Servicios o herramientas necesarios
- MongoDB

# Entorno de desarrollo
La aplicación se desarrolló en python 3.9.4, para la ejecución del código se necesita configurar un archivo .env en la raiz del projecto el cual contiene las siguientes variables de entorno

connection_mongo_db = "Aquí connection string Mongo DB"
mongo_db_name = "APP_BOOKING"
connection_communication_services = "Aquí la connection string de Azure communication services"

Es necesario instalar las dependencias del documento requirements.txt por lo que es recomendable instalarlas en un entorno virtual `python -m venv .venv` y posteriormente `pip install -r requirements.txt`.

Finalmente para ejecutar la aplicación use el comando uvicorn `uvicorn main:app`, esta es una aplicación fastAPI, por tanto puede acceder a swagger en http://localhost:8000/docs

# Suposiciones

- Solo se puede registrar un peluquero siempre que se le asigne alguno de los siguientes servicios "Service 1", "Service 2", "Service 3".
- Cada reserva puede tener los siguientes status "Created", "Finished"
- El tiempo minimo de reserva es de 30min y maximo 120min, y además debe ser multiplo de 30min, es decir, 13:00, 13:30, 14:00 son valores validos. Adem
- Solo se pueden reservar fechas futuras, tenga en cuenta que la zona horaria es America/Bogota
- Solo se enviará la notificación de creación de reservación al cliente
- Por simplicidad la fecha y hora se manejan con el siguiente formato "%Y-%m-%d %H:%M:%S" (Hora militar), además se ignora la zona horaria.
- Se supone que la aplicación es stateless y no maneja ningún tipo de autenticación y autorización por ende el servicio para finalizar una cita reservada debe enviar id y el mail del peluquero, de este modo se validará que al menos el correo del peluquero coincida con la reserva para él
