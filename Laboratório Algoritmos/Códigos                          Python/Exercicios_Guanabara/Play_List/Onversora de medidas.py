unidades = float(input("digite uma ditancia em metros:"))
km = unidades / 1000
hm = unidades / 100
dc = unidades * 100
dm = unidades * 10
cm = unidades * 100
mm = unidades * 1000
print("Quilometros: {}. Hêctometros: {}. Decâmetros: {}. Decimetros:{} Centimetros: {}. millimetros: {}.".format(km,hm,dc,dm,cm,mm))