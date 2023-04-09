# Obtener el valor del token y el tiempo restante antes de que caduque
token_value = ourjson['token']
expiration_time = ourjson['expiration_time']

# Calcular el tiempo restante en segundos y convertirlo a minutos
time_remaining = expiration_time - int(time.time())
minutes_remaining = time_remaining // 60

# Imprimir el valor del token y el tiempo restante en minutos
print(f"El valor del token es: {token_value}")
print(f"El tiempo restante antes de que caduque el token es de: {minutes_remaining} minutos")
