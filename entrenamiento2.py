nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario: "))
if precio_unitario < 1:
  print("Precio no válido")
else:
    cantidad = int(input("Cantidad de productos adquiridos: "))
if cantidad < 1:
  print("Cantidad no válida")
else:
    porcentaje_dcto = float(input("Ingrese el porcentaje de descuento: "))
    if porcentaje_dcto < 1 and porcentaje_dcto > 100:
        print("Porcentaje erróneo")
    else:
        costo_sin_descuento = precio_unitario * cantidad
        valor_porcentaje = (costo_sin_descuento * porcentaje_dcto) / 100
        costo_con_descuento = costo_sin_descuento - valor_porcentaje
        costo_con_descuento = round(costo_con_descuento, 2)
        print(f"\nCompraste {cantidad} {nombre_producto} a un precio unitario de: {precio_unitario}") 
        print (f"lo cual tendria un valor de {costo_sin_descuento}")
        print(f"El valor total de la compra con descuento es {costo_con_descuento} ya que tuvo un descuento de {round(valor_porcentaje, 2)}")
