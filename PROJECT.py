
# BY AAYUSH PATEL ,K22LR ,ROLL.no 56 #
import random #it is imported to generate a random number from the provided range
head="WELCOME TO RANDOM INTEGER GENERATOR"
print(head.center(95,"_"))
a = int(input("Enter starting of range: "))#this is the input for starting of the range.


b = int(input("Enter ending of range: "))#this is the number which is last number of the range.

isPrime = True
num = random.randint(a,b)
print("The selected number {} is:".format(num))#will print the randomly selected number.  
if(num >= 0):#now if the selected number is greater or equal to zero then it will print positive.
    print("         1. Positive")
else:#now if the selected number is smaller than  zero then it will print negative.
    print("         1. Negative")

if(num%2 == 0):#if the selected number is perfectly  divisible by 2 then it is even .
    print("         2. Even")
else:#if the selected number is  not perfectly  divisible by 2 then it is odd .
    print("         2. Odd")
#now for the number to be a prime number is must be positive.
if num >= 0:
    for i in range(2,num+1):
        if num % i == 0:#now i is a number  starting  from 2 to the number itself i.e., its range is from (2,num+1)
            #if the number is divisible by any other number than itself than it is not a prime number 
            isPrime = False
            break #this will break the loop and the numbner will come out of the loop
    #if the number dosent satisfy the above condition it will come here.
    if isPrime:
        print("         3. is Prime")
    else:
        print("         3. is not Prime")
else:
    print("         3. Negative numbers are not prime")#as we know negative numbers are not prime numbers.
l="THANK YOU"
print(l.center(59,"!"))