
n = int(input("Enter length of sequence? "))
n1, n2 = 0, 1
cnt = 0

if n <= 0:
   print("Invalid Input")
elif n == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while cnt < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       cnt += 1
