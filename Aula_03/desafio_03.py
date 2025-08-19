## Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

def CalculoBonus():
    nome = False
    salario = False
    Bônus = False
    
    while not nome:
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
    while not salario:
        try:
            salario = float(input('Digite seu salário: '))
            if salario < 0:
                print('Por favor, digite um salário positivo')
        except ValueError:
            print('Entrada inválida para o salário')
    while not Bônus:
        try:
            Bônus = float(input('Qual é o percentual do seu bônus? ').replace("%","")) / 100
            if Bônus < 0:
                print('Digite um valor de Bônus válido')
        except ValueError:
            print('Entrada inválida para o Bônus')
    
    resultado = 1000 + (salario * (Bônus + 1))
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${resultado:.2f}.")


CalculoBonus()

