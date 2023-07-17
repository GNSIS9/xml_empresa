# -*- coding: utf-8 -*-
#XPath en Python.  #Busqueda parametrizada. 

from lxml import etree
# Parsear el archivo XML
documento = etree.parse("empleados.xml")
# Solicitar el ID del empleado
id_empleado = input("Ingrese el ID del empleado: ")
# Construir la expresión XPath
xpath_expression = f"//empleado[@id='{id_empleado}']/nombre/text()"
# Obtener el nombre del empleado
nombre_empleado = documento.xpath(xpath_expression)
# Verificar si se encontró un empleado con el ID dado
if nombre_empleado:
    print(f"Nombre del empleado con ID {id_empleado}: {nombre_empleado[0]}")
else:
    print("No se encontró ningún empleado con el ID especificado.")