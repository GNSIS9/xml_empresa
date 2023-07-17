
from lxml import etree

def leer_fichero(xml_file):
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    
    # Obtener los elementos de los empleados
    empleados = xml_tree.xpath("//empleados/empleado")

    for empleado in empleados:
        nombre = empleado.find("nombre").text
        sueldo = float(empleado.find("salario").text)
        if sueldo >= 3000:
            print("Nombre:", nombre)
            print("Salario:", sueldo)
            print("---")

# Ruta al archivo XML
xml_file = "empleados.xml"

# Llamar a la función para leer el archivo XML
leer_fichero(xml_file)

