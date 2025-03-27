# For loop example
sum = 0
list = (6, 5, 2)
for i in list:
    sum += i  # Instead of sum = sum + 1
print("The sum of the list is: ", sum)

# While loop example
i = 0
while i <= 3:
    i += 1
    print("*")

# Loop with break
for val in "string":
    print('in loop', val)
    if val == "i":
        break
print('out of loop', val)