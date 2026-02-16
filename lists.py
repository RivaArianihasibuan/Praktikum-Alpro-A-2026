thislist = ["apple", "banana", "cherry"]
print(thislist)

#nilai duplikat

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#panjang daftar 

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Daftar Item - Tipe Data

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Konstruktor list()

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access List Items

thislist = ["apple", "banana", "cherry"]

#Pengindeksan Negatif

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Rentang Indeks Negatif

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Change List Items

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Mengubah Rentang Nilai Item

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#sisipkan item

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add List Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Perluas Daftar

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Tambahkan Iterable Apa Pun

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

##Remove List Items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Hapus Indeks yang Ditentukan

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Bersihkan Daftar

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Lists

thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)

#Lakukan perulangan melalui nomor indeks.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#Menggunakan Loop While

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#Perulangan Menggunakan List Comprehension 

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#Sintaksis

newlist = [x for x in fruits if x != "apple"]

#Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Urutkan Menurun

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#Sesuaikan Fungsi Pengurutan

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Urutan Terbalik

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)





