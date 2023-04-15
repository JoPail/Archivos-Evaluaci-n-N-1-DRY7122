#		SCRIPT PARA IMPRIMIR TOKEN Y TIEMPO DE CADUCIDAD DEL MISMO

#	IMPORTAMOS BIBLIOTECA JSON Y ESTABLECER COMO VARIABLE
import json

with open("/home/devasc/labs/devnet-src/parsing/myfile.json", "r") as json_file:
	ourjson = json.load(json_file)

token = ourjson["access_token"]
caducidad = ourjson["expires_in"]

#	IMPRIMIR LA INFORMACIÓN
print("TOKEN: ", token)
print("TIEMPO DE CADUCIDAD: ", caducidad)
