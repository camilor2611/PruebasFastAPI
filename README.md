# Entorno de desarrollo
pipenv 2023.11.17

# Suposiciones

- Solo se puede registrar un peluquero siempre que se le asigne alguno de los siguientes servicios "Service 1", "Service 2", "Service 3".
- El tiempo minimo de reserva es de 30min y maximo 60min
- Por simplicidad la fecha y hora se manejan con el siguiente formato "%Y-%m-%d %H:%M:%S", además se ignora la zona horaria.
- Se supone que la aplicación es stateless y no maneja ningún tipo de autenticación y autorización por ende el servicio para finalizar una cita reservada debe enviar id y el mail del peluquero, de este modo se validará que al menos el correo del peluquero coincida con la reserva para él

