import math
def g1_function(x):
    Sum = 0
    Sum2 = 0
    for k in range (0,11):
        Sum += (x ** (2 * k + 1))/(math.factorial(2*k+1))
        Sum2 += (x ** (3 * k)) / (math.factorial(3 * k))

    g = Sum / Sum2
    return g

y = int(input("Введите натуральное y: "))
print("The resulting y is ", (1.7 * g1_function(0.25) + 2 * g1_function(1 + y))/(6 - g1_function(y ** 2 - 1)))