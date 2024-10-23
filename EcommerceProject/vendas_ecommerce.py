import pandas as pd

class VendasEcommerce:
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
        Remove valores nulos, ajusta tipos e prepara os dados.
        """
        self.dados.dropna(inplace=True)
        self.dados['preco'] = self.dados['preco'].astype(float)
        self.dados['custo'] = self.dados['custo'].astype(float)
        print("Dados limpos e prontos para uso.")

    def filtrar_categoria(self, categoria):
        """
        Filtra os dados por uma categoria específica.
        :param categoria: Categoria de produto para filtrar.
        :return: DataFrame filtrado pela categoria.
        """
        filtrado = self.dados[self.dados['categoria'] == categoria]
        return filtrado

    def calcular_lucro(self):
        """
        Cria uma nova coluna 'lucro' com o cálculo do lucro por pedido (preço de venda - custo).
        """
        if 'preco' in self.dados.columns and 'custo' in self.dados.columns:
            self.dados['lucro'] = self.dados['preco'] - self.dados['custo']
            print("Coluna de lucro criada com sucesso.")
        else:
            print("Colunas 'preco' ou 'custo' não existem nos dados.")