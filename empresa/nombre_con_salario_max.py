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
    
    # Obtener el nombre del empleado con el salario máximo
    nombre_max = next(empleado.find("nombre").text for empleado in empleados if float(empleado.find("salario").text) == salario_maximo)
    
    return salario_maximo, nombre_max

# Ruta al archivo XML
xml_file = "empleados.xml"

# Obtener el salario máximo y el nombre del empleado
salario_maximo, empleado_maximo = obtener_salario_maximo(xml_file)

print("Salario máximo:", salario_maximo)
print("Empleado con salario máximo:", empleado_maximo)
