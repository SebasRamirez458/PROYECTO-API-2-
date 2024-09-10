def obtener_datos_usuario():
    nombre_departamento = input("INGRESE EL NOMBRE DEL DEPARTAMENTO QUE DESEA CONSULTAR: ").upper()
    limite_registros = int(input("INGRESE EL LIMITE DE REGISTROS QUE DESEA CONSULTAR: "))
    municipio = input("INGRESE EL NOMBRE DEL MUNICIPIO QUE DESEA CONSULTAR: ").upper()
    cultivo = input("INGRESE EL NOMBRE DEL CULTIVO QUE DESEA CONSULTAR: ")
    datos_ingresados = [nombre_departamento, municipio, cultivo, limite_registros]
    return datos_ingresados

def mostrar_datos(datos):
    print(datos)


    