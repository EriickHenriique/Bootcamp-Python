#Desafio - Refatorar o projeto da aula anterior evitando Bugs!
#Para resolver os bugs identificados
#  tratamento de entradas inválidas que não podem ser convertidas para um número de ponto flutuante
#  e prevenção de valores negativos para salário e bônus, você pode modificar o código diretamente.
#  Isso envolve adicionar verificações adicionais após a tentativa de conversão para garantir
#  que os valores sejam positivos.

def CalculoBonus():
    try:
        nome = input('Digite seu nome completo: ')
        if len(nome) == 0:
            raise ValueError('O nome não pode estar vazio')
        elif any(char.isdigit() for char in nome):
            raise ValueError('Nome não pode conter digito')
        else:
            print('Nome válido: ', nome)
    except ValueError as e:
        print(e)

    try:
        salario = float(input('Digite seu salário: '))
        if salario < 0:
            print('Por favor, digite um salário positivo')
    except ValueError:
        print('Entrada inválida para o salário')
    
    try:
        Bônus = float(input('Qual é o percentual do seu bônus? ').replace("%","")) / 100
        if Bônus < 0:
            print('Digite um valor de Bônus válido')
    except ValueError:
        print('Entrada inválida para o Bônus')
    
    resultado = 1000 + (salario * (Bônus + 1))
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${resultado:.2f}.")


CalculoBonus()







