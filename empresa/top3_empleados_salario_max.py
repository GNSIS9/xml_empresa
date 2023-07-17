
from lxml import etree

def leer_fichero(xml_file):
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    
    # Obtener los empleados ordenados por salario en orden descendente
    empleados = xml_tree.xpath("//empleados/empleado")
    empleados.sort(key=lambda e: float(e.xpath("salario")[0].text), reverse=True)
    
    # Obtener los tres empleados con los salarios más altos
    empleados_top = empleados[:3]
    
    # Imprimir los empleados con los salarios más altos
    print("Los tres empleados con los salarios más altos:")
    for empleado in empleados_top:
        nombre = empleado.xpath("nombre")[0].text
        salario = empleado.xpath("salario")[0].text
        print("Nombre:", nombre)
        print("Salario:", salario)
        print("---")

# Ruta al archivo XML
xml_file = "empleados.xml"

# Llamar a la función para leer el archivo XML y obtener los tres empleados con los salarios más altos
leer_fichero(xml_file)
