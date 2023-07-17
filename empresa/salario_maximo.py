
from lxml import etree

def obtener_salario_maximo(xml_file):
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    
    # Obtener los elementos de los empleados
    empleados = xml_tree.xpath("//empleados/empleado")
    
    # Obtener los salarios como una lista de números
    salarios = [float(empleado.find("salario").text) for empleado in empleados]
    
    # Obtener el salario máximo
    salario_maximo = max(salarios)
    
    return salario_maximo

# Ruta al archivo XML
xml_file = "empleados.xml"

# Obtener el salario máximo
salario_maximo = obtener_salario_maximo(xml_file)

print("Salario máximo:", salario_maximo)
