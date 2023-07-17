
#XPath en Python. Acceso a los atributos en XPATH con @. #Obtener los identificadores de los empleados:
from lxml import etree

# Parsear el archivo XML
documento = etree.parse("empleados.xml")
empleados = documento.xpath("//empleado/@id")
print(empleados)