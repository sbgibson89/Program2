for number in range(10):
    print(number+1)

sum_of_all = 0
counter = 1
while counter <= 100:
    sum_of_all = sum_of_all + counter
    counter = counter + 1
print("Sum of all numbers up to 100 is " + str(sum_of_all))

for number in range(0, 21, 2):
    print(number)

for i in range (1, 11):
    print ("5 x " + str(i) + " = " + str(i*5))

x = 10
countdown = ""
while x >= 1:
    if x == 1:
        countdown = countdown + str(x)
    else:
        countdown = countdown + str(x) + ","
    x = x - 1
print (countdown)