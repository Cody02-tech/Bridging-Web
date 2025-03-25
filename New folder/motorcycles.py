motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)

motocycles[0]='ducati'
print(motocycles)

motocycles.append('honda')
print(motocycles)


motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

motocycles = ['honda', 'yamaha', 'suzuki']
motocycles.insert(0, 'ducati')
print(motocycles)

print('After deleting element at index 0')
del motocycles[0]
print(motocycles)

poped_motocycle = motocycles.pop()
print(f"remainig motocycles after pop call {motocycles}")
print(f"poped motocycle {poped_motocycle}")
print(motocycles)
print(f" poped element {motocycles.pop(0)}")
print(f"remaining element {motocycles}")