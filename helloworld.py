a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','U','V','W','X','Y','Z',' ']
b="HELLO WORLD"
c=''
for i in b:
  for j in a:
    if j==i:
      c+=j
      print(c)
