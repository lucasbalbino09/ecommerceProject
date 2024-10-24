import pandas as pd

class Moves:
    def __init__(self):
        self.dados = pd.DataFrame()

    def carregar_dados(self, caminho):
        """
        Carrega os dados de um arquivo CSV para o dataframe 'dados'.
        :param caminho: Caminho para o arquivo CSV.
        """
        self.dados = pd.read_csv(caminho)
        print("Dados carregados com sucesso.")

    def limpar_dados(self):
        """
        Remove valores nulos e prepara os dados.
        """
        # Remove valores nulos
        self.dados.dropna(inplace=True)
        print("Dados limpos e prontos para uso.")

    def filtrar_categoria(self, categoria):
        """
        Filtra os dados por uma categoria específica no campo 'averageRating'.
        :param categoria: Valor de averageRating para filtrar.
        :return: DataFrame filtrado pela categoria.
        """
        filtrado = self.dados[self.dados['averageRating'] == categoria]
        return filtrado

    def calcular_lucro(self):
        """
        Exemplo de cálculo de lucro (modificado para se adequar aos dados).
        Já que o CSV fornecido não contém 'preco' ou 'custo', essa função foi adaptada.
        """
        # Apenas um exemplo de cálculo com base em numVotes, pode adaptar conforme necessário.
        if 'numVotes' in self.dados.columns:
            self.dados['lucro_simulado'] = self.dados['numVotes'] * 0.01  # Cálculo de lucro
            print("Coluna de lucro simulado criada com sucesso.")
        else:
            print("Coluna 'numVotes' não existe nos dados.")

# Caminho para o arquivo CSV
caminho_arquivo = 'data.csv'

# Instanciando a classe e utilizando as funções
vendas = Moves()
vendas.carregar_dados(caminho_arquivo)
vendas.limpar_dados()

# Exemplo de filtragem por 'averageRating'
filtrados = vendas.filtrar_categoria(9.5)
print(filtrados)

# Exemplo de cálculo de lucro (simulado)
vendas.calcular_lucro()
print(vendas.dados)
