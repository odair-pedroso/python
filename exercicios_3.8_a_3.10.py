# 3.8 pense em cinco lugares do mundo que vc gostaria de visitar

#armazene os locais em uma lista

lugares = ['Itália','Espanha','Holanda','Austrália','Maldivas']
print(lugares)

print(sorted(lugares))
print(lugares)

lugares.reverse()
print(lugares)

lugares.sort(reverse=True)
print(lugares)

# Escolha uma das listas dos exercicios e exiba uma mensagem informando o numero de pessoas que vc esta convidando para o jantar

convidados = ['Odair','Tamara','Duda']
print(len(convidados))

numero_pessoas_convidadas = len(convidados)
print(numero_pessoas_convidadas)
numero_pessoas_convidadas = str(len(convidados))

message = 'O número de pessoas que estou convidando para o jantar são : ' + numero_pessoas_convidadas

print(message)
