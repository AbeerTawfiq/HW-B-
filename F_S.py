numterms = int(input("How many terms? "))
num1, num2 = 0, 1
count = 0


if numterms <= 0:
   print("Please enter a positive number")

elif numterms == 1:
   print("Fibonacci sequence upto",numterms,":")
   print(num1)

else:
   print("Fibonacci sequence:")
   while count < numterms:
       print(num1)
       next_num = num1 + num2
   
       num1 = num2
       num2 = next_num
       count += 1