#   Inteiros (int)
# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.

def SomaInt():
    soma1 = int(input('Digite o primeiro número: '))
    soma2 = int(input('Digite o segundo número: '))
    resultado = soma1 + soma2
    return print(resultado)

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

def RestoInt():
    num = int(input('Digite um número: '))
    resultado = num % 5
    return print(f'O resultado final é {resultado}')

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

def MultInt():
    resultado = print('O resultado da multiplicação é: ' + str(int(input('Digite um número: ')) * int(input('Digite outro número: '))))
    return resultado

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

def DivInt():
    resultado = print('O resultado da divisão é: ' + str(int(input('Digite um número: ')) // int(input('Digite outro número: '))))
    return resultado

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

def RaizInt():
    num = int(input('Digite um número: '))
    resultado = print(num ** 2)
    return resultado


#   Números de Ponto Flutuante (float)
# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição.
def SomaFloat():
    soma1 = float(input('Digite o primeiro número: '))
    soma2 = float(input('Digite o segundo número: '))
    resultado = soma1 + soma2
    return print(resultado)

# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
def MediaFloat():
    media1 = float(input('Digite o primeiro número: '))
    media2 = float(input('Digite o segundo número: '))
    resultado = (media1 + media2) / 2
    return print(resultado)

# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
def PotenciaFloat():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite a potencia desejada número: '))
    resultado = num1 ** num2
    return print(resultado)

# 9 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.
def TempFloat():
    num1 = float(input('Digite o primeiro número: '))
    resultado = (num1 * 1.8) + 32
    return print(resultado)

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o raio do círculo: "))
def RaioFloat():
    raio = float(input("Digite o raio do círculo: "))
    area = 3.14159 * raio ** 2
    resultado = print("A área do círculo é:", area)
    return resultado

#   Strings (str)
# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

def StringUpper():
    text = str(input('Digite um frase minuscula: '))
    resultado = print(f'A frase {text} em maiusculo ficará: {text.upper()}')
    return resultado

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
def StringLower():
    text = str(input('Digite seu nome Completo: '))
    resultado = print(f'A frase {text} em maiusculo ficará: {text.lower()}')
    return resultado

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
def StringStrip():
        text = str(input('Digite uma frase: '))
        resultado = print(text.strip())
        return resultado
 
# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
def DataStr():
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    dia, mes, ano = data.split("/")
    print("Dia:", dia)
    print("Mês:", mes)
    print("Ano:", ano)

# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.
def ConcatStr():
    frase1 = str(input("Digite uma palavra: "))
    frase2 = str(input("Digite outra palavra: "))
    resultado = print(frase1 + ' é ' + frase2)
    return resultado

#   Booleanos (bool)
# 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
def ResultAnd():
    valor1 = True
    valor2 = False
    resultado_and = valor1 and valor2
    print("Resultado do AND lógico:", resultado_and)

# 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
def ResultOr():
    valor1 = True
    valor2 = False
    resultado_or = valor1 or valor2
    print("Resultado do AND lógico:", resultado_or)

# 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
def ResultNot():
    valor1 = True
    valor2 = False
    resultado_not = not valor1
    print("Resultado do AND lógico:", resultado_not)

# 19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
def numigual():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    resultado = print(num1 == num2)
    return resultado


# 20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
def numdif():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um número: '))
    resultado = print(num1 != num2)
    return resultado