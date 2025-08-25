# Crie quatro variáveis usando Type Hint representando:
#sua idade (int),
#sua altura (float),
#seu nome (str)
#se você gosta de programar em Python (bool).
#Depois, imprima uma frase combinando essas informações.

def exercicio_01():
    idade: int = 27
    altura: float = 1.60
    nome: str = 'Erick'
    gosta_python: bool = True
    print(f'Meu nome é {nome} e tenho {idade} anos com {altura}cm de altura. E é {gosta_python} que gosto de Python')

#Implemente uma função chamada calcular_imposto que recebe dois parâmetros:
#salário (float)
#taxa (float, default 0.1)
#e retorna o valor do imposto a ser pago. Use Type Hint nos parâmetros e no retorno da função.

def calcular_imposto():
    salario: float = 1000
    taxa: float = 0.1
    imposto_a_ser_pago: float = salario * taxa
    return imposto_a_ser_pago

#4. Lista ao Quadrado
#Crie uma lista de números de 1 a 20.
#  Usando um loop for, crie outra lista contendo apenas os quadrados desses números.


def exercicio_04():
    quadrados = []
    lista = list(range(1,21))
    for num in lista:
        quadrado = num ** 2
        quadrados.append(quadrado)
    print(quadrados)

#Dada a lista ["Python", "Java", "C++", "JavaScript"]:
#Remova "Java"
#Adicione "Go"
#Inverta a ordem da lista

def exercicio_05():
    lista = ["Python", "Java", "C++", "JavaScript"]
    lista.remove('Java')
    lista.append('Go')
    lista = lista[::-1]
    print(lista)

#Crie um dicionário chamado produto com as chaves: "nome", "preço", "estoque".
#Atualize o preço do produto para um valor maior.
#Adicione uma nova chave "categoria".
#Imprima o dicionário final.

def exercicio_06():
    dicionario = {'nome': 'Sabão',
                'preço': 20,
                'estoque': 'A'}
    dicionario.update({'nome': 'Sabão',
                'preço': 22,
                'estoque': 'A'})
    dicionario['Categoria'] = 'Limpeza'
    print(dicionario)

#Escreva uma função que receba uma string e retorne um dicionário com a contagem de cada palavra.
#Exemplo: "engenharia de dados é dados"
#Resultado esperado: {"engenharia": 1, "de": 1, "dados": 2, "é": 1}

def exercicio_07(texto):
    texto = texto.lower()
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] =+ 1
    print(contagem)

#Dada a lista de compras ["maçã", "banana", "cereja", "maçã"] 
# e o dicionário de preços {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total considerando as repetições.

def exercicio_08():
    lista = ["maçã", "banana", "cereja", "maçã"]
    dicionário = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
    total = 0    
    for item in lista:
        total += dicionário[item]
    print(total)

#Crie uma função chamada filtrar_pares que recebe uma lista de inteiros e retorna apenas os números pares.
#Use List Comprehension dentro da função.

def filtrar_pares(lista):
    numeros_pares = [item for item in lista if item % 2 == 0]
    print(numeros_pares)

#Implemente uma função chamada pares_que_somam que recebe uma lista de números e um número alvo,
#  e retorna todas as combinações de pares que somam ao alvo.
#Exemplo:
#Entrada: [2, 4, 3, 5, 7], alvo = 7
#Saída: [(2, 5), (4, 3)]
        
def pares_que_somam(nums: list[int], alvo: int) -> list[tuple[int, int]]:
    vistos: set[int] = set()
    pares_unicos: set[tuple[int, int]] = set()

    for n in nums:
        comp = alvo - n
        if comp in vistos:
            par = tuple(sorted((n, comp))) 
            pares_unicos.add(par)
        vistos.add(n)

    return sorted(pares_unicos) 


        
    








