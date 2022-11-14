

reggeli = {'tea', 'vaj', 'piritós'}
ebed = set()
ebed = set(['halászlé', 'kenyér', True, True])  
print(type(ebed))
print(ebed)

reggeli.add('víz')
# reggeli.remove('körte')
reggeli.discard('körte')    
print(reggeli)


reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}
print(reggeli & ebed)
print(reggeli | ebed)
print(reggeli - ebed)
print(reggeli ^ ebed)
    
gyumolcskosar=['eper','alma','szilva','eper']
fajta=set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)