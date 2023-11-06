# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
for i in range(1,5):
    nome = str(input("Digite um nome: "))
    idade = int(input("Digite uma idade: "))
    sexo = str(input("Digite 'M' para masculino \n ou \n digite 'F' para feminino: "))
    