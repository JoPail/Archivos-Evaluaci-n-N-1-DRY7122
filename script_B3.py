#	SCRIPT QUE INDICA QUÉ TIPO DE ACL IPV4 ES SEGÚN DATOS OTORGADOS

#	SOLICITAR ACL IPV4
num_acl = input("Ingrese el número de ACL IPv4: ")

#	CONVERTIR NÚMERO A ENTERO
num_acl = int(num_acl)

#		TIPOS DE ACL

#	ESTÁNDAR
if 1 <= num_acl <= 99:
	print("El número de ACL", num_acl, "es de tipo ESTÁNDAR")

#	EXTENDIDA
elif 100 <= num_acl <= 199:
	print("El número de ACL", num_acl, "es de tipo EXTENDIDA")

else:
	print("El número de ACL", num_acl, "no corresponde a una lista de acceso")
