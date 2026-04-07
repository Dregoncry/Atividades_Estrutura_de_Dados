class No:
    def __init__(self, dado: any):
        self.dado:any = dado
        self.dir: No = None
        self.esq: No = None
    
    
class Lista_Duplamente_Encadeada:
    def __init__(self):
        self.tamanho: int = 0
        self.inicio: No = None
        self.fim: No = None

    def inserir_final(self, valor):
        valor = No(valor)

        if self.tamanho == 0:
            self.inicio = valor
        
        else:
            valor.esq = self.fim
            self.fim.dir = valor

        self.fim = valor
        self.tamanho += 1

    def inserir_inicio(self, valor):
        valor = No(valor)

        if self.tamanho == 0:
            self.fim = valor

        else:
            valor.dir = self.inicio
            self.inicio.esq = valor

        self.inicio = valor
        self.tamanho += 1

    def inserir_posicao(self, valor, posicao):
        if posicao < 0 or posicao > self.tamanho:
            print("Posição inválida")
            return

        if posicao == 0:
            self.inserir_inicio(valor)
            return

        if posicao == self.tamanho:
            self.inserir_final(valor)
            return

        valor = No(valor)
        aux = self.inicio

        for _ in range(posicao - 1):
            aux = aux.dir

        valor.esq = aux
        valor.dir = aux.dir
        aux.dir.esq = valor
        aux.dir = valor
        self.tamanho += 1

    def imprimir(self):
        if self.inicio is None:
            print("Lista vazia")
            return

        aux = self.inicio
        
        while aux is not None:
            print(f"{aux.dado}", end=" ")
            aux = aux.dir
        print()

    def remover(self, dado):
        aux = self.inicio

        while aux is not None and aux.dado != dado:
            aux = aux.dir

        if aux is None:
            return False

        if aux.esq is None:
            self.inicio = aux.dir
        else:
            aux.esq.dir = aux.dir

        if aux.dir is None:
            self.fim = aux.esq
        else:
            aux.dir.esq = aux.esq

        self.tamanho -= 1
        return True



def main():
    lista = Lista_Duplamente_Encadeada()

    while True:
        print()
        print("===== MENU - LISTA DUPLAMENTE ENCADEADA =====")
        print("1. Inserir no inicio")
        print("2. Inserir no final")
        print("3. Inserir em uma posicao")
        print("4. Remover dado")
        print("5. Imprimir lista")
        print("0. Sair")

        opcao = input("Escolha uma opcao: ")

        match opcao:
            case "1":
                entrada = input("Digite o valor: ")
                lista.inserir_inicio(entrada)
                print()
                print("Valor inserido no inicio.")

            case "2":
                entrada = input("Digite o valor: ")
                lista.inserir_final(entrada)
                print()
                print("Valor inserido no final.")

            case "3":
                entrada = input("Digite o valor: ")
                posicao = int(input("Digite a posicao (0 ate tamanho): "))
                lista.inserir_posicao(entrada, posicao)
                print()
                print(f"Valor inserido na posicao {posicao}.")

            case "4":
                dado = input("Digite o dado a remover: ")
                removido = lista.remover(dado)
                if removido:
                    print()
                    print("Dado removido com sucesso.")
                else:
                    print()
                    print("Dado nao encontrado na lista.")

            case "5":
                print()
                print("Lista atual:")
                lista.imprimir()

            case "0":
                print()
                print("Encerrando o programa.")
                break

            case _:
                print()
                print("Opcao invalida. Tente novamente.")

if __name__ == "__main__":
    main()