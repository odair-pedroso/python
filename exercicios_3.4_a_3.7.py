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