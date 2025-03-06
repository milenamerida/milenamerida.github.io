n1, n2 = 0, 1
n3 = 0

print("Fibonacci series: {},".format(n2),end=" ")
for i in range (0,19):
        n3 = n1 + n2
        print("{},".format(n3), end=" ")
        n1 = n2
        n2 = n3
