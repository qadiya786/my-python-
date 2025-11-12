num = int(input("enter the number"))
if num < 0:
  print("enter the number")
else:
  sum_numbers = 0
  counter = 1
  while counter <= num:
    sum_numbers += counter
    counter += 1
print("the sum_natural number is:" , sum_numbers)
