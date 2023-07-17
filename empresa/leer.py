#Consulta con XPATH: los 3 libros publicados mรกs recientemente:
from lxml import etree

def leer_fichero(xml_file):
   
  # Cargar el archivo XML
    xml_tree = etree.parse(xml_file)
    print(xml_tree)
    
  #empl = xml_tree.xpath("//libros/libro")
    empleados = xml_tree.xpath("//empleados/empleado")


    for empleado in empleados:
        nombre = empleado.find("nombre").text
        print("nombre:", nombre)
       

# Ruta al archivo XML y DTD
xml_file = "empleados.xml"

# Llamar a la funciรณn para validar el XML con el DTD
leer_fichero(xml_file)