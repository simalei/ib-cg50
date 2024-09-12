aam =   float(input("Avg A M: "))
i1 =    float(input("I1: "))
i2 =    float(input("I2: "))

x = aam * 100 - i2 * 100 # rhs
y = i2 - i1 # lhs

percent_i1 = abs(x/y)
percent_i2 = 100 - percent_i1

print("I1 abun:", percent_i1)
print("I2 abun:", percent_i2)

