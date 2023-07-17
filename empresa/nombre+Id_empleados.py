# -*- coding: utf-8 -*-
 #Obtener los nombres e identificadores de los empleados:

from lxml import etree

# Parsear el archivo XML
documento = etree.parse("empleados.xml")
empleados = documento.xpath("//empleado")
for empleado in empleados:
    nombre = empleado.xpath("nombre/text(1)")[0]
    empleado_id = empleado.xpath("@id")[0]
    print(f"Nombre: {nombre}, ID: {empleado_id}")