# take input
operation =  input("""Para convertir de Bolívar Soberano a 
Bolívar Digital escriba 'D' 
Para convertir de Bolívar Digital a 
Bolívar digital escriba 'S': """).upper()

while operation == "D":
    print ("Introduzca la cantidad en Bolívar Soberano, si es decimal, coloque punto")
    d = float(input()) #input by user
    y = 1000000
    digital = "La cantidad en bolívar digital es: "
    print(digital + str(d/y))
if operation == "S":
    print ('Introduzca la cantidad en Bolívar Digital, si es decimal, coloque punto')
    s = float(input()) #input by user
    y = 1000000
    soberano = "La cantidad en bolívar soberano es: "
    print(soberano + str(s*y))
else:
  print("Gracias por usar la calculadora")