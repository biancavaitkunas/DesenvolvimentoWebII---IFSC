class Produto:

    def __init__(self, codigo, descricao, autor, preco, qtdEstoque):
        self.codigo = codigo
        self.descricao = descricao
        self.autor = autor
        self.preco = preco
        self.qtdEtoque = qtdEstoque

    def __str__(self):
        return f"""
        === Produto ===
        Código: {self.codigo}
        Descrição: {self.descricao}
        Autor: {self.autor}
        Preço: {self.preco}
        Qtd. Estoque: {self.qtdEtoque}
        """