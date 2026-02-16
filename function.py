#Membuat Fungsi

def my_function():
  print("Hello from a function")

#Memanggil sebuah Fungsi

def my_function():
  print("Hello from a function")

my_function()

def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

#Menggunakan Fungsi

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

#Nilai Kembalian

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

#Pernyataan Lulus

def my_function():
  pass

#Python Function Arguments

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#parameter vs argumen

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

#Jumlah Argumen

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

#Nilai Parameter Default

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

#Argumen Kata Kunci

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

#Argumen Posisional

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

#Mencampur Argumen Posisi dan Argumen Kata Kunci

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#Meneruskan Berbagai Tipe Data

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Nilai Kembalian

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

#Mengembalikan Tipe Data yang Berbeda

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#Argumen Hanya Berdasarkan Posisi

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

#Argumen Khusus Kata Kunci

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

#Berdasarkan Posisi Saja dan Pencarian Berdasarkan Kata Kunci Saja

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)