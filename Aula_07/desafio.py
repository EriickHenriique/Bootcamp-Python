from typing import Dict, List
import csv
from collections import defaultdict

#Ler o arquivo CSV e carregar os dados.
#Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, 
# cada um contendo informações do produto (Produto, Quantidade, Venda).
#Calcular o total de vendas (Quantidade * Venda) por categoria.
#Funções
#Ler CSV:

#Função: ler_csv
#Entrada: Nome do arquivo CSV
#Saída: Lista de dicionários com dados lidos
#Processar Dados:

arquivo2 = 'Aula_07/vendas.csv'



def ler_csv(arquivo):
    with open(arquivo, mode="r", encoding='utf-8') as lido:
        leitor = csv.DictReader(lido)
        resultado = list(leitor)
        return resultado


#Função: processar_dados
#Entrada: Lista de dicionários
#Saída: Dicionário processado conforme descrito

def processar_dados(resultado):
    categorias = defaultdict(list)
    for linha in resultado:
        categoria = linha["Categoria"]
        produto_info = {
            'Produto': linha['Produto'],
            'Quantidade': linha['Quantidade'],
            'Venda': linha['Venda']
        }
        categorias[categoria].append(produto_info)
    return dict(categorias)


#Calcular Vendas por Categoria:
##Função: calcular_vendas_categoria
##Entrada: Dicionário processado
##Saída: Dicionário com total de vendas por categoria


def calcular_vendas_categoria(processado: Dict[str, List[Dict[str, str]]]):
    totais = {}

    for categoria, produtos in processado.items():
        qtd_total = 0
        venda_total = 0

        for linha in produtos:
            qtd = int(linha['Quantidade'])
            venda = float(linha['Venda'])
            qtd_total += qtd
            venda_total += qtd * venda

        totais[categoria] = {
            "Quantidade": qtd_total,
            "Venda": venda_total
        }

    return print(totais)


resultado = ler_csv(arquivo2)
resultado2 = processar_dados(resultado)
resultado3 = calcular_vendas_categoria(resultado2)