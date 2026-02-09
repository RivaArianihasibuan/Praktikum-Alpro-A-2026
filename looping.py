#python while loops

#loop while

i = 1
while i < 6:
  print(i)
  i += 1

#pernyataan jeda

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#pernyataan lanjutan

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#pernyataan else

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#python for loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#perulangan sebuah string

for x in "banana":
  print(x)

#pernyataan jeda

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#pernyataan lanjutan

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#fungsi range

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x) 

#jika tidak, dalam perulangan for

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#perulangan bersarang

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pernyataan lulus

for x in [0, 1, 2]:
  pass    







