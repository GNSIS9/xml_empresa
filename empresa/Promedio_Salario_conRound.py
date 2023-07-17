
#XPath en Python. Salario promedio utilizando la función sum() de XPath y el operador div.

from lxml import etree

# Parsear el archivo XML
documento = etree.parse("empleados.xml")
salario_promedio = documento.xpath("round(sum(//empleado/salario) div count(//empleado/salario))")
print(f"Salario promedio: {salario_promedio}")

