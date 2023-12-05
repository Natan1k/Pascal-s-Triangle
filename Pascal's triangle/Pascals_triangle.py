import math

def combination(n,r):
    combination_value = math.factorial(n)/(math.factorial(n-r)*math.factorial(r))
    return combination_value

n = int(input("\nEnter the max number of rows: "))
print("\n\n\n")
Row = []

#Calculates all the values of the pascals triangle
for x in range(n):
    Row_hold = []
    for y in range(x+1):
        Row_hold.append(str(int(combination(x,y))))
    Row.append(Row_hold)

#Calculates the maximum length(base length) the trinage can have
Base_length = len(" ".join(Row[n-1]))

#Makes the shape of a triange by adding spaces
for x in range(n):
    Current_Row = " ".join(Row[x])
    diff = Base_length - len(Current_Row)
    space = int(diff/2) * " "
    print(space + Current_Row)

input()