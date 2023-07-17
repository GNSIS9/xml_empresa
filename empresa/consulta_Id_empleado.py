# -*- coding: utf-8 -*-
from lxml import etree

# Parsear el archivo XML
documento = etree.parse("empleados.xml")

# Definir el número de empleados a consultar
num_empleados = 1

empleados = documento.xpath("//empleado")
for i, empleado in enumerate(empleados[:num_empleados]):
    nombre = empleado.xpath("nombre/text()")[0]
    empleado_id = empleado.xpath("@id")[0]
    print(f"Nombre: {nombre}, ID: {empleado_id}")

    # Detener el bucle después de consultar el número deseado de empleados
    if i + 1 == num_empleados:
        break
