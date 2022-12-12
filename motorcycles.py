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

# removendo elementos através do pop

motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

popped_motocycle = motorcycles.pop()
print(motorcycles)
print(popped_motocycle)

# exemplo de uso do pop()

motorcycles = ['honda', 'yamaha','suzuki']
last_owned = motorcycles.pop()

print(' A última motocicleta que tive foi a ' + last_owned.title() + ".")

# escolhendo o elemento da lista a ser removido com pop()

motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)
first_owned = motorcycles.pop(0)
print(first_owned)


print(' A primeira motocicleta que tive foi a '+ first_owned.title() + ".")

# removendo um item de acordo com o valor usando metodo remove()

motorcycles = ['honda', 'yamaha','suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha','suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA " + too_expensive.title() + " é muito cara .")







