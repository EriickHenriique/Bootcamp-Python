from typing import List

#Tarefa: Crie uma função chamada calcular_media que recebe uma lista de números flutuantes
# e retorna a média aritmética desses valores.
#  A função deve incluir type hints para os parâmetros e para o retorno.

listax = [8, 5, 10, 4, 6, 8, 3, 2, 1]
def calcular_media(valores: List[float]) -> float:
    resultado: float = sum(valores) / len(valores)
    return print(resultado)

#Tarefa: Crie uma função chamada filtrar_acima_de que recebe uma lista de números flutuantes
#  e um valor limite. A função deve retornar uma nova lista contendo apenas os números que são estritamente
# maiores que o limite. Adicione type hints para todos os parâmetros e para o retorno.

def filtrar_acima_de(valor_flutuante: List[float], valor_limite: int) -> List[float]:
    resultado: List[float] = []
    for num in valor_flutuante:
        if num > valor_limite:
            resultado.append(num)
    return print(resultado)

#Tarefa: Crie uma função chamada contar_valores_unicos que recebe uma lista de números inteiros.
#  A função deve retornar a quantidade de valores únicos presentes nessa lista.
#  Inclua type hints para os parâmetros e para o retorno.

def contar_valores_unicos(valores: List[int]) -> List[int]:
    return print(len(set(valores)))


#Tarefa: Crie uma função chamada celsius_para_fahrenheit que recebe uma lista de temperaturas em graus Celsius
#  (números flutuantes). A função deve retornar uma nova lista com as temperaturas convertidas para Fahrenheit,
#  utilizando a fórmula F = (9/5) * C + 32. Adicione type hints para os parâmetros e para o retorno.

def celcius_para_fahrenheit(temp: List[float]) -> List[float]:
    temperaturas: List[float] = []
    for num in temp:
        fahr = (num * 9/5) + 32
        temperaturas.append(fahr)
    return print(temperaturas)

#Tarefa: Crie uma função chamada calcular_desvio_padrao que recebe uma lista de números flutuantes.
#  A função deve calcular e retornar o desvio padrão desses valores. 
# Inclua type hints para os parâmetros e para o retorno.

def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

#Tarefa: Crie uma função chamada encontrar_valores_ausentes que recebe uma lista de números inteiros
#  que representam uma sequência (por exemplo, [1, 2, 4, 5]).
#  A função deve identificar e retornar uma lista com os valores que estão ausentes na sequência,
#  considerando o intervalo do menor ao maior número presente na lista original.
#  Adicione type hints para os parâmetros e para o retorno.


lista2 = [1,2,3,5,7,9]

def encontrar_valores_ausentes(valores: List[int]) -> List[int]:
    menor = min(valores)
    maior = max(valores)
    lista = list(range(menor,maior))
    resultado: List[float] = []
    for num in lista:
        if num not in valores:
            resultado.append(num)
    return print(resultado)





