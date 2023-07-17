from datetime import datetime
from lxml import etree

def leer_fichero(xml_file):
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    
    # Obtener los elementos de los empleados que nacieron antes de 1985
    empleados = xml_tree.xpath("//empleados/empleado[number(substring(fecha_nac, 7)) < 1985]")
    
    for empleado in empleados:
        nombre = empleado.find("nombre").text
        fecha_nac_str = empleado.find("fecha_nac").text
        fecha_nac = datetime.strptime(fecha_nac_str, "%d/%m/%Y")
        print(nombre, fecha_nac.strftime("%d/%m/%Y"))

# Ruta al archivo XML
xml_file = "empleados.xml"

# Llamar a la función para leer el archivo XML
leer_fichero(xml_file)
 