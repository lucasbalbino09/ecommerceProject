import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dragon_moves import Moves

vendas = Moves()
# caminho correto do dataset
file_path = os.path.join(os.getcwd(), 'data.csv')
vendas.carregar_dados(file_path)  

vendas.limpar_dados()

categoria_filtrada = vendas.filtrar_categoria(9.5)  
print(categoria_filtrada)

# Salvar o resultado filtrado em um arquivo .txt
with open("resultado_filtrado.txt", "w") as file:
    file.write(categoria_filtrada.to_string(index=False))  # Salva o DataFrame como string no arquivo
print("Resultado filtrado salvo em 'resultado_filtrado.txt'.")

vendas.calcular_lucro()

print(vendas.dados.head())

# Salva o DataFrame como string no arquivo
with open("dados_com_lucro.txt", "w") as file:
    file.write(vendas.dados.to_string(index=False))  
print("Dados com lucro salvo em 'dados_com_lucro.txt'.")
