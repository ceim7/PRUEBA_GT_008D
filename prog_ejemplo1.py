import random

nom_eq1 = ""
nom_eq2 = ""
nom_eq3 = ""
nom_eq4 = ""
nom_eq5 = ""
nom_eq6 = ""
punt_eq1 = 0
punt_eq2 = 0
punt_eq3 = 0
punt_eq4 = 0
punt_eq5 = 0
punt_eq6 = 0

nom_eq1 = input("Ingrese nombre de  equipo 1 ")
nom_eq2 = input("Ingrese nombre de  equipo 2 ")
nom_eq3 = input("Ingrese nombre de  equipo 3 ")
nom_eq4 = input("Ingrese nombre de  equipo 4 ")
nom_eq5 = input("Ingrese nombre de  equipo 5 ")
nom_eq6 = input("Ingrese nombre de  equipo 6 ")


# partido eq1 vs eq2 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq1 = punt_eq1 + 3
elif resultado == 1:
    punt_eq1 = punt_eq1 + 1
    punt_eq2 = punt_eq2 + 1
elif  resultado == 2:
    punt_eq2 = punt_eq2 + 3

# partido eq1 vs eq3 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq1 = punt_eq1 + 3
elif resultado == 1:
    punt_eq1 = punt_eq1 + 1
    punt_eq3 = punt_eq3 + 1
elif  resultado == 2:
    punt_eq3 = punt_eq3 + 3

# partido eq1 vs eq4 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq1 = punt_eq1 + 3
elif resultado == 1:
    punt_eq1 = punt_eq1 + 1
    punt_eq4 = punt_eq4 + 1
elif  resultado == 2:
    punt_eq4 = punt_eq4 + 3

# partido eq1 vs eq5 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq1 = punt_eq1 + 3
elif resultado == 1:
    punt_eq1 = punt_eq1 + 1
    punt_eq5 = punt_eq5 + 1
elif  resultado == 2:
    punt_eq5 = punt_eq5 + 3

# partido eq1 vs eq6 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq1 = punt_eq1 + 3
elif resultado == 1:
    punt_eq1 = punt_eq1 + 1
    punt_eq6 = punt_eq6 + 1
elif  resultado == 2:
    punt_eq6 = punt_eq6 + 3

# partido eq2 vs eq1 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq2 = punt_eq2 + 3
elif resultado == 1:
    punt_eq2 = punt_eq2 + 1
    punt_eq1 = punt_eq1 + 1
elif  resultado == 2:
    punt_eq1 = punt_eq1 + 3

# partido eq2 vs eq3 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq2 = punt_eq2 + 3
elif resultado == 1:
    punt_eq2 = punt_eq2 + 1
    punt_eq3 = punt_eq3 + 1
elif  resultado == 2:
    punt_eq3 = punt_eq3 + 3

# partido eq2 vs eq4 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq2 = punt_eq2 + 3
elif resultado == 1:
    punt_eq2 = punt_eq2 + 1
    punt_eq4 = punt_eq4 + 1
elif  resultado == 2:
    punt_eq4 = punt_eq4 + 3

# partido eq2 vs eq5 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq2 = punt_eq2 + 3
elif resultado == 1:
    punt_eq2 = punt_eq2 + 1
    punt_eq5 = punt_eq5 + 1
elif  resultado == 2:
    punt_eq5 = punt_eq5 + 3

# partido eq2 vs eq6 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq2 = punt_eq2 + 3
elif resultado == 1:
    punt_eq2 = punt_eq2 + 1
    punt_eq6 = punt_eq6 + 1
elif  resultado == 2:
    punt_eq6 = punt_eq6 + 3

# partido eq3 vs eq1 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq3 = punt_eq3 + 3
elif resultado == 1:
    punt_eq3 = punt_eq3 + 1
    punt_eq1 = punt_eq1 + 1
elif  resultado == 2:
    punt_eq1 = punt_eq1 + 3


# partido eq3 vs eq2 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq3 = punt_eq3 + 3
elif resultado == 1:
    punt_eq3 = punt_eq3 + 1
    punt_eq2 = punt_eq2 + 1
elif  resultado == 2:
    punt_eq2 = punt_eq2 + 3

    
# partido eq3 vs eq4 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq3 = punt_eq3 + 3
elif resultado == 1:
    punt_eq3 = punt_eq3 + 1
    punt_eq4 = punt_eq4 + 1
elif  resultado == 2:
    punt_eq4 = punt_eq4 + 3

    
# partido eq3 vs eq5 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq3 = punt_eq3 + 3
elif resultado == 1:
    punt_eq3 = punt_eq3 + 1
    punt_eq5 = punt_eq5 + 1
elif  resultado == 2:
    punt_eq5 = punt_eq5 + 3

    
# partido eq3 vs eq6 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq3 = punt_eq3 + 3
elif resultado == 1:
    punt_eq3 = punt_eq3 + 1
    punt_eq6 = punt_eq6 + 1
elif  resultado == 2:
    punt_eq6 = punt_eq6 + 3

    
# partido eq4 vs eq1 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq4 = punt_eq4 + 3
elif resultado == 1:
    punt_eq4 = punt_eq4 + 1
    punt_eq1 = punt_eq1 + 1
elif  resultado == 2:
    punt_eq1 = punt_eq1 + 3


# partido eq4 vs eq2 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq4 = punt_eq4 + 3
elif resultado == 1:
    punt_eq4 = punt_eq4 + 1
    punt_eq2 = punt_eq2 + 1
elif  resultado == 2:
    punt_eq2 = punt_eq2 + 3


# partido eq4 vs eq3 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq4 = punt_eq4 + 3
elif resultado == 1:
    punt_eq4 = punt_eq4 + 1
    punt_eq3 = punt_eq3 + 1
elif  resultado == 2:
    punt_eq3 = punt_eq3 + 3

    # partido eq4 vs eq5 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq4 = punt_eq4 + 3
elif resultado == 1:
    punt_eq4 = punt_eq4 + 1
    punt_eq5 = punt_eq5 + 1
elif  resultado == 2:
    punt_eq5= punt_eq5 + 3


    # partido eq4 vs eq6 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq4 = punt_eq4 + 3
elif resultado == 1:
    punt_eq4 = punt_eq4 + 1
    punt_eq6 = punt_eq6 + 1
elif  resultado == 2:
    punt_eq6 = punt_eq6 + 3

# partido eq5 vs eq1 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq5 = punt_eq5 + 3
elif resultado == 1:
    punt_eq5 = punt_eq5 + 1
    punt_eq1 = punt_eq1 + 1
elif  resultado == 2:
    punt_eq1 = punt_eq1 + 3


    # partido eq5 vs eq2 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq5 = punt_eq5 + 3
elif resultado == 1:
    punt_eq5 = punt_eq5 + 1
    punt_eq2 = punt_eq2 + 1
elif  resultado == 2:
    punt_eq2 = punt_eq2 + 3
    

    # partido eq5 vs eq3 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq5 = punt_eq5 + 3
elif resultado == 1:
    punt_eq5 = punt_eq5 + 1
    punt_eq3 = punt_eq3 + 1
elif  resultado == 2:
    punt_eq3 = punt_eq3 + 3
    
    # partido eq5 vs eq4 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq5 = punt_eq5 + 3
elif resultado == 1:
    punt_eq5 = punt_eq5 + 1
    punt_eq4 = punt_eq4 + 1
elif  resultado == 2:
    punt_eq4 = punt_eq4 + 3

    
    # partido eq5 vs eq6 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq5 = punt_eq5 + 3
elif resultado == 1:
    punt_eq5 = punt_eq5 + 1
    punt_eq6 = punt_eq6 + 1
elif  resultado == 2:
    punt_eq6 = punt_eq6 + 3


    # partido eq6 vs eq1 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq6 = punt_eq6 + 3
elif resultado == 1:
    punt_eq6 = punt_eq6 + 1
    punt_eq1 = punt_eq1 + 1
elif  resultado == 2:
    punt_eq1 = punt_eq1 + 3
    

    # partido eq6 vs eq2 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq6 = punt_eq6 + 3
elif resultado == 1:
    punt_eq6 = punt_eq6 + 1
    punt_eq2 = punt_eq2 + 1
elif  resultado == 2:
    punt_eq2 = punt_eq2 + 3

        # partido eq6 vs eq3 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq6 = punt_eq6 + 3
elif resultado == 1:
    punt_eq6 = punt_eq6 + 1
    punt_eq3 = punt_eq3 + 1
elif  resultado == 2:
    punt_eq3 = punt_eq3 + 3

        # partido eq6 vs eq4 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq6 = punt_eq6 + 3
elif resultado == 1:
    punt_eq6 = punt_eq6 + 1
    punt_eq4 = punt_eq4 + 1
elif  resultado == 2:
    punt_eq4 = punt_eq4 + 3

        # partido eq6 vs eq5 
resultado = random.randrange(3)
if resultado == 0:
    punt_eq6 = punt_eq6 + 3
elif resultado == 1:
    punt_eq6 = punt_eq6 + 1
    punt_eq5 = punt_eq5 + 1
elif  resultado == 2:
    punt_eq5 = punt_eq5 + 3


print("El puntaje del equipo 1 es ",punt_eq1)
print("El puntaje del equipo 2 es ",punt_eq2)
print("El puntaje del equipo 3 es ",punt_eq3)
print("El puntaje del equipo 4 es ",punt_eq4)
print("El puntaje del equipo 5 es ",punt_eq5)
print("El puntaje del equipo 6 es ",punt_eq6)

puntaje_max =  max(punt_eq1,punt_eq2,punt_eq3,punt_eq4,punt_eq5,punt_eq6)

if puntaje_max == punt_eq1:
   print("El equipo ",nom_eq1, " es el Campeon ")
if puntaje_max == punt_eq2:
   print("El equipo ",nom_eq2, " es el Campeon ")
if puntaje_max == punt_eq3:
   print("El equipo ",nom_eq3, " es el Campeon ")
if puntaje_max == punt_eq4:
   print("El equipo ",nom_eq4, " es el Campeon ")
if puntaje_max == punt_eq5:
   print("El equipo ",nom_eq5, " es el Campeon ")
if puntaje_max == punt_eq6:
   print("El equipo ",nom_eq6, " es el Campeon ")
