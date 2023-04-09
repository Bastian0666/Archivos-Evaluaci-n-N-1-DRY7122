# Solicitar el número de ACL IPv4 al usuario
numero_acl = input("Ingrese el número de ACL IPv4: ")

# Verificar si el número de ACL IPv4 es una ACL Estándar, Extendida o no corresponde a una lista de acceso
if int(numero_acl) >= 1 and int(numero_acl) <= 99:
    print("El número de ACL IPv4 " + numero_acl + " corresponde a una ACL Estándar.")
elif int(numero_acl) >= 100 and int(numero_acl) <= 199:
    print("El número de ACL IPv4 " + numero_acl + " corresponde a una ACL Extendida.")
else:
    print("El número de ACL IPv4 " + numero_acl + " no corresponde a una lista de acceso.")
