#Desafio_01

NomeColaborador = str(input('Qual é o seu nome? '))
Salário = float(input('Qual é o seu salário? '))
Bônus = float(input('Qual é o percentual do seu bônus? ').replace("%","")) / 100
resultado = 1000 + (Salário * (Bônus + 1))

print(f'Olá, {NomeColaborador}! seu salário + bônus é de R$ {resultado} reais')