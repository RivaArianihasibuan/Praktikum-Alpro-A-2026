#list
thislist = [75, 80, 65, 90, 85]
thislist.append(95)
print(thislist)
thislist.remove(65)
print(thislist)
thislist.sort()
print(thislist)


print(thislist)

#tuple
thistuple = {"D00", "Dr.Andi", "Struktur Data", 12}
print(thistuple[1])#nama dosen
print(thistuple[2])#mata kuliah diampu
for x in thistuple:
     print(x)

y = list(thistuple)
y[3] = 14
thistuple = tuple(y)
print(thistuple)
#kelebihan tuple dibanding list adalah tuple lebih simple

#list
keahlian_A = {"python", "java", "SQL", "Git"}
Keahlian_B = {"python","C++", "Dokter"}
myset = keahlian_A.interection(keahlian_B)#keahlian A&B



