# Introducción
Esta API está enfocada en la asignación de citas de clientes con su peluquero de preferencia 

# Servicios o herramientas necesarios
- MongoDB
- Azure Communication Services
- Azure Web App

# Entorno de desarrollo
La aplicación se desarrolló en python 3.9.4, para la ejecución del código se necesita configurar un archivo .env en la raíz del proyecto el cual contiene las siguientes variables de entorno

mongo_db_name = "APP_BOOKING"

connection_mongo_db = "Aquí connection string Mongo DB"
connection_communication_services = "Aquí la connection string de Azure communication services"

Es necesario instalar las dependencias del documento requirements.txt por lo que es recomendable instalarlas en un entorno virtual `python -m venv .venv` y posteriormente `pip install -r requirements.txt`.

Finalmente para ejecutar la aplicación use el comando uvicorn `uvicorn main:app`, esta es una aplicación fastAPI, por tanto puede acceder a swagger en http://localhost:8000/docs

# Suposiciones

- Solo se puede registrar un peluquero siempre que se le asigne alguno de los siguientes servicios "Service 1", "Service 2", "Service 3".
- El campo phone es de 10 dígitos
- Cada reserva puede tener los siguientes status "Created", "Finished"
- El tiempo mínimo de reserva es de 30min y máximo 120min, y además debe ser multiplo de 30min, es decir, 13:00, 13:30, 14:00 son valores válidos. Además, por cada solicitud solo se puede reservar un servicio del peluquero
- Solo se pueden reservar fechas futuras, tenga en cuenta que la zona horaria es America/Bogota
- Solo se enviará la notificación de creación de reservación al cliente
- No puede haber reservaciones sobrepuestas en tiempo
- Por simplicidad la fecha y hora se manejan con el siguiente formato "%Y-%m-%d %H:%M:%S" (Hora militar), además se ignora la zona horaria.
- Se supone que la aplicación es stateless y no maneja ningún tipo de autenticación y autorización por ende el servicio para finalizar una cita reservada debe enviar id y el mail del peluquero, de este modo se validará que al menos el correo del peluquero coincida con la reserva para él

# Testing

Para realizar el testing se debe instalar `pip install -r requirements_dev.txt` y ejecutar `pytest` los test realizan una consulta directa a los endpoints y se realizan los siguientes test

- Se verifica que cree un cliente y se registre correctamente en DB (test_client.py)
- Se intenta insertar un cliente con un correo no válido (test_client.py)
- Se verifica que cree un peluquero y se registre correctamente en DB (test_hairdresser.py)
- Se verifica que no puede insertar un servicio para un peluquero fuera de la lista ["Service 1", "Service 2", "Service 3"] (test_booking.py)
- Se valida la creación de cliente y peluquero y que el cliente pueda agendar una reservación, finalmente, se actualiza la reservación a estado finalizada (test_booking.py). Aunque podemos decir que esto no es una prueba unitaria es importante vailidar el flujo y la relación que hay entre los diferentes endpoints
