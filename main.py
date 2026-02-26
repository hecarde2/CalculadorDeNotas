# CalculadorDeNotas
nombre = input("Nombre del estudiante")
nota1 = float(input("ingrese primnera nota"))
nota2 = float(input("ingrese segunda nota"))
nota3 = float(input("ingrese tercera nota"))

# Promedio 
promedio = ( nota1 + nota2 + nota3) / 3
print(f"El promedio del estudiantes {nombre}, es: {promedio}" )

# Aprobo o no 
if promedio >= 70:
    print("aprobado :)")
else :
    print("reprobo :()")