N = int(input("Enter a number : "))
counter = 1
evensum = 0
oddsum = 0
evencount = 0
while(counter < N+1):
    if(counter % 2) == 0:
        evensum = evensum + counter
        evencount = evencount + 1
    else:
        oddsum = oddsum + counter
    counter = counter +1
print("Even avarage is ", int(evensum/evencount))
print("Odd sum is ", oddsum)