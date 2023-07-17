

from lxml import etree

# Parsear el archivo XML
documento = etree.parse("empleados.xml")

empleados = documento.xpath("//empleados/empleado[position()=3]")
# Imprimir el nombre y apellido de los empleados
for empleado in empleados:
    nombre = empleado.find("nombre").text
    apellido = empleado.find("apellido").text
    print(f"Empleado: {apellido} {nombre}")
