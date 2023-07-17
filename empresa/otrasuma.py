
import os
from lxml import etree

def leer_fichero(xml_file):
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    xml_file = os.path.abspath("empleados.xml")
    
    # Obtener los elementos de los empleados
    empleados = xml_tree.xpath("//empleados/empleado")

    # Obtener los salarios como una lista de valores
    salarios = [float(empleado.find("salario").text) for empleado in empleados]

    # Calcular la suma total de salarios utilizando la función sum
    suma_total = sum(salarios)

    print("Suma total de salarios:", suma_total)

# Ruta al archivo XML
xml_file = "empleados.xml"

# Llamar a la función para leer el archivo XML y calcular la suma de salarios
leer_fichero(xml_file)
