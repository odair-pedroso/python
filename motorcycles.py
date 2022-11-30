# Alterar dados de ula lista

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

# Concatenando elementos no final de uma lista

motorcycles = ['honda', 'yamaha','suzuki', 'ducati']
print(motorcycles)

motorcycles.append('kawasaki')
print(motorcycles)

# iniciando com uma lista vazia e adicionando elementos

motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('kawasaki')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
motorcycles.append('ducati')
print(motorcycles)

# inserindo elementos em uma lista ( em qualquer posição da lista com metodo insert)

motorcycles = ['honda', 'yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles.insert(1,'kawasaki')
print(motorcycles)

# removendo elementos de uma lista usando a função del

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)










