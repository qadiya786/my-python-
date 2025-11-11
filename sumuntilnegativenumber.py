total = 0
while True:
  n = int(input("enter the number: "))
  if n < 0:
    break
  total += n
print("sum is " , total)
