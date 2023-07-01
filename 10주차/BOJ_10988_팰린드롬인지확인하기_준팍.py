s = input()

if len(s) == 1:
  print(1)
else:
  for i in range(len(s)//2):
    if s[i] != s[(i+1)*-1]:
      print(0)
      break
    elif i == len(s)//2-1 :
      print(1)
