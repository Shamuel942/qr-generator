import qrcode
import os
import webbrowser

#URL que quisieras convertir en QR
url = input("Introduce el enlace que quieras convertir en qr")

#Ruta donde se guardara el PNG(QR_FY)
ruta_carpeta = os.path.expanduser("C:\\Users\\Shamuel\\Desktop\\QR")
nombre_archivo = "Mi_QR.png"
ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

#Generar el codigo QR
qr = qrcode.make(url)
qr.save(ruta_completa)

#Mostrar mensaje y abrir imagen
print(f"Codigo QR guardado en: {ruta_completa}")
webbrowser.open(ruta_completa)
input("Pulsa Enter para cerrar....")
