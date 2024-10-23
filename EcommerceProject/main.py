# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Criar uma instância da classe VendasEcommerce
from vendas_ecommerce import VendasEcommerce

vendas = VendasEcommerce()

# Passo 1: Carregar os dados
vendas.carregar_dados('dataset.csv')  # Use o caminho correto do seu dataset

# Passo 2: Limpar os dados
vendas.limpar_dados()

# Passo 3: Filtrar por uma categoria específica
categoria_filtrada = vendas.filtrar_categoria('Eletronicos')
print(categoria_filtrada)

# Passo 4: Calcular lucro
vendas.calcular_lucro()

# Visualizar os dados com a nova coluna 'lucro'
print(vendas.dados.head())
