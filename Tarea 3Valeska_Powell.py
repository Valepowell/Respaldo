#Carga de Datos:
#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
#«producto»: una cadena de texto que represente el nombre del producto vendido.
#«cantidad»: un número entero que represente la cantidad de productos vendidos.
#«precio»: un número flotante que represente el precio unitario del producto.

ventas = [
     {"fecha": "2025-05-01", "producto": "Piña", "cantidad": 200, "precio": 100.0},
     {"fecha": "2025-05-01", "producto": "Uva", "cantidad": 250, "precio": 250.0},
     {"fecha": "2025-05-02", "producto": "Plátanos", "cantidad": 300, "precio": 350.0},
     {"fecha": "2025-05-02", "producto": "Naranjas", "cantidad": 350, "precio": 240.0},
     {"fecha": "2025-05-03", "producto": "Peras", "cantidad": 400, "precio": 300.0},
     {"fecha": "2025-05-05", "producto": "Peras", "cantidad": 250, "precio": 150.0},
     {"fecha": "2025-05-05", "producto": "Uva", "cantidad": 250, "precio": 200.0},
]

#Cálculo de Ingresos Totales:
#Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas.
# Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

ingresos_totales =0
for venta in ventas:
   ingresos_totales +=venta["cantidad"]*venta["precio"]

print("Los Ingresos Totales Son:", ingresos_totales)


#Análisis del Producto Más Vendido:
#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos 
# y los valores sean la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad
producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

print("Producto más vendido:", producto_mas_vendido)
print("Cantidad total vendida:", ventas_por_producto[producto_mas_vendido])

#Promedio de Precio por Producto:
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas.
# Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
ventas_promedio = {}
repeticiones = 0
for venta in ventas:
    producto = venta["producto"]
    total_por_venta = venta["cantidad"]*venta["precio"]
    repeticiones = venta["cantidad"]
    if producto not in precios_por_producto:
        precios_por_producto[producto] = [0, 0]
    precios_por_producto[producto][0] += total_precio
    precios_por_producto[producto][1] += cantidad

precios_promedio = {}
for producto, (suma, total) in precios_por_producto.items():
    precios_promedio[producto] = suma / total

print("Precios promedio por producto:")
for producto, promedio in precios_promedio.items():
    print(f"{producto}: {promedio:.2f}")

#Ventas por Día:
#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    ingresos_por_dia[fecha] = ingresos_por_dia.get(fecha, 0) + ingreso

print("Ingresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: {ingreso}")


#Representación de Datos:
#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados.
# Cada diccionario anidado debe contener:
#«cantidad_total»: la cantidad total vendida del producto.
#«ingresos_totales»: los ingresos totales generados por la venta del producto.
#«precio_promedio»: el precio promedio de venta del producto.

resumen_ventas = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso = venta["cantidad"] * venta["precio"]
    if producto not in resumen_ventas:
        resumen_ventas[producto] = {"cantidad_total": 0, "ingresos_totales": 0.0, "precio_promedio": 0.0}
    resumen_ventas[producto]["cantidad_total"] += venta["cantidad"]
    resumen_ventas[producto]["ingresos_totales"] += ingreso

for producto in resumen_ventas:
    total_ingreso = resumen_ventas[producto]["cantidad_total"]
    ingresos = resumen_ventas[producto]["ingresos_totales"]
    resumen_ventas[producto]["precio_promedio"] = ingresos / total_ingreso

print("Resumen de ventas:")
for producto, info in resumen_ventas.items():
    print(f"{producto}: {info}")