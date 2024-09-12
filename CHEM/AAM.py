isotopes = []
fin = False
i = 1

while not fin:
    mass = input("I" + str(i) + " M: ")
    try:
        mass = float(mass)
    except ValueError:
        fin = True
    else:
        ratio = float(input("I" + str(i) + " %: "))
        isotopes.append((mass, ratio))
        i = i + 1


int_sum = 0.0

for pair in isotopes:
    int_sum = int_sum + pair[0] * pair[1]

print("AAM:", int_sum/100)

    

    
