    #1
halmaz1 = {'A', 'B', 'C'}
halmaz1.clear()

#2
halmaz2 = {"D","E","F"}
halmaz3 = halmaz2.copy()
print(halmaz3)

#3
halmaz4 = {"G","H","I"}
halmaz5 = {"K","L","M"}
halmaz4.difference(halmaz5)
print(halmaz4)

#4
halmaz6 = {"N","O","P"}
halmaz7 = {"Q","R","S"}
halmaz6.update(halmaz7)
print(halmaz6)

#5
halmaz8 = {"T","U","V"}
halmaz9 = {"W","X","Y"}
halmaz8.intersection(halmaz9)
print(halmaz8)

#6
halmaz10 = {"Z","a","b"}
halmaz11 = {"c","d","e"}
halmaz10.intersection_update(halmaz11)
print(halmaz10)

#7
halmaz12 = {"f","g","h"}
halmaz13 = {"i","j","k"}
print(halmaz12.isdisjoint(halmaz13))

#8
halmaz14 = {"l","m","n"}
halmaz15 = {"o","p","q"}
print(halmaz14.issubset(halmaz15)," Benen van-e ez a halmaz egy másikba?")

#9
halmaz16 = {"r","s","t"}
halmaz17 = {"u","v","w"}
print(halmaz16.issuperset(halmaz17)," Benen van-e egy másik halmaz ebben?")

#10
halmaz18 = {"x","y","z"}
halmaz19 = {"1","2","3"}
print(halmaz18.symmetric_difference(halmaz19)," Visszadob egy halmazt egy szimmetrikus különbséggel.")

#11
halmaz20 = {"4","5","6"}
halmaz21 = {"7","8","9"}
print(halmaz20.pop())
print(halmaz21.add("10"))
print(halmaz20.union(halmaz21))