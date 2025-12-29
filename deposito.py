class Deposito:
    def adicionar_estoque(self, produto, quantidade):
        produto.quantidade += quantidade

    def retirar_estoque(self, produto, quantidade):
        if quantidade <= produto.quantidade:
            produto.quantidade -= quantidade
            return True
        else:
            print("Estoque Insificiente")
            return False
