from lxml import etree

def leer_fichero(xml_file):
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    
    # Obtener los elementos de los empleados
    empleados = xml_tree.xpath("//empleados/empleado[departamento='Ventas']")

    for empleado in empleados:
        nombre = empleado.find("nombre").text
        apellido = empleado.find("apellido").text
        salario = empleado.find("salario").text
        departamento = empleado.find("departamento").text
        print(nombre, apellido, salario, departamento)
          

# Ruta al archivo XML
xml_file = "empleados.xml"

# Llamar a la función para leer el archivo XML
leer_fichero(xml_file)

