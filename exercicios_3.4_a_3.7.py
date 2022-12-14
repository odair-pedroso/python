lista_de_convidados = ['Odair', 'Tamara', 'Maria Eduarda', 'Rosangela', 'Matheus','Vera', 'Ana','Silvana','Carlos']

message0 = 'Bem vindo , convidado ' + lista_de_convidados[0]
message1 = 'Bem vindo, convidado '+ lista_de_convidados[1]
message2 = 'Bem vindo, convidado '+ lista_de_convidados[2]

print(message0)
print(message1)
print(message2)

print('Carlos')
lista_de_convidados[8] = 'Marcelo'

print(lista_de_convidados)

message0='Bem vindo , convidado ' + lista_de_convidados[0]
message1='Bem vindo , convidado ' + lista_de_convidados[1]
message2='Bem vindo , convidado ' + lista_de_convidados[2]
message3='Bem vindo , convidado ' + lista_de_convidados[3]
message4='Bem vindo , convidado ' + lista_de_convidados[4]
message5='Bem vindo , convidado ' + lista_de_convidados[5]
message6='Bem vindo , convidado ' + lista_de_convidados[6]
message7='Bem vindo , convidado ' + lista_de_convidados[7]

print(message0)
print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message7)

novo_convidado_1 = 'Duda'
novo_convidado_2 = 'Zanza'
novo_convidado_3 = 'Marcelo'

message8 = "Olá "+ novo_convidado_1 + ", " + novo_convidado_2 + ", " + novo_convidado_3 + ", temos mais uma mesa para acomodar vocês."
print (message8)

print (lista_de_convidados)

lista_de_convidados.insert(0,novo_convidado_1)

lista_de_convidados.insert(4,novo_convidado_2)

lista_de_convidados.append(novo_convidado_3)

print(lista_de_convidados)

message9 = "Boa noite , infelizmente só poderemos chamar 2 convidados devido ao espaço disponível."
print (message9)

convidado_excluido_1= lista_de_convidados.pop(11)
print("Boa noite ," + convidado_excluido_1 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_2= lista_de_convidados.pop(10)
print("Boa noite ," + convidado_excluido_2 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_3= lista_de_convidados.pop(9)
print("Boa noite ," + convidado_excluido_3 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_4= lista_de_convidados.pop(8)
print("Boa noite ," + convidado_excluido_4 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_5= lista_de_convidados.pop(7)
print("Boa noite ," + convidado_excluido_5 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_6= lista_de_convidados.pop(6)
print("Boa noite ," + convidado_excluido_6 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_7= lista_de_convidados.pop(5)
print("Boa noite ," + convidado_excluido_7 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_8= lista_de_convidados.pop(4)
print("Boa noite ," + convidado_excluido_8 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_9= lista_de_convidados.pop(3)
print("Boa noite ," + convidado_excluido_9 + " sinto muito em não poder de convidar para jantar!!")

convidado_excluido_10= lista_de_convidados.pop(2)
print("Boa noite ," + convidado_excluido_10 + " sinto muito em não poder de convidar para jantar!!")

print(lista_de_convidados)

print("Boa noite " + lista_de_convidados[0] + " você esta convidada para o jantar!")
print("Boa noite " + lista_de_convidados[1] + " você esta convidada para o jantar!")

print(lista_de_convidados)

print(lista_de_convidados[0])
print(lista_de_convidados[1])

del lista_de_convidados[0]
print(lista_de_convidados)
del lista_de_convidados[0]

print(lista_de_convidados)

