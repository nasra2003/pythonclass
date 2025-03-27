
# Program to Add Natural Numbers
n = int(input("Enter how many natural numbers you want to add: "))
sum = 0 
i = 1

while i <= n:
    sum += i
    i += 1

print("The sum of the first", n, "natural numbers is:", sum)