
from lxml import etree
def leer_fichero(xml_file):
   
    # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    salarios = xml_tree.xpath("sum(//empleados/empleado/salario)")
    print(salarios)

    
# Ruta al archivo XML y DTD
xml_file = "empleados.xml"

# Llamar a la función para validar el XML con el DTD
leer_fichero(xml_file)