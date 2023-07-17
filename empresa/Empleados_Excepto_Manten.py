

#XPath en Python. Seleccionar todos los empleados que NO pertenezcan al departamento "Mantenimiento".

from lxml import etree

# Parsear el archivo XML
documento = etree.parse("empleados.xml")

empleados = documento.xpath("//empleado[not(departamento = 'Mantenimiento')]")
# Imprimir el nombre y apellido de los empleados
for empleado in empleados:
    nombre = empleado.find("nombre").text
    apellido = empleado.find("apellido").text
    print(f"Empleado: {nombre} {apellido}")