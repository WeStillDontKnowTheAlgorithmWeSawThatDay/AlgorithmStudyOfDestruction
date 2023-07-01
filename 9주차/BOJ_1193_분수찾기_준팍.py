n = int(input())

layer = 0
last_number = 0

while n > last_number:
  layer += 1
  last_number += layer
  
if layer % 2 == 1:
  numerator = last_number - n + 1
  denominator = layer - last_number + n
  print(f'{numerator}/{denominator}')
else :
  numerator = layer - last_number + n
  denominator = last_number - n + 1
  print(f'{numerator}/{denominator}')
  