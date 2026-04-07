from LDPE import Lista_Duplamente_Encadeada


class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None
        self.ant = None


class ListaCircularDupla:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir_final(self, dado):
        novo = No(dado)

        if self.inicio is None:
            self.inicio = novo
            novo.prox = novo
            novo.ant = novo
        else:
            ultimo = self.inicio.ant

            ultimo.prox = novo
            novo.ant = ultimo

            novo.prox = self.inicio
            self.inicio.ant = novo

        self.tamanho += 1

    def remover_no(self, no):
        if self.tamanho == 1:
            self.inicio = None
        else: 
            no.ant.prox = no.prox
            no.prox.ant = no.ant

            if no == self.inicio:
                self.inicio = no.prox

        self.tamanho -= 1


class Processo:
    def __init__(self, id_processo, nome, tempo_total):
        self.id_processo = id_processo
        self.nome = nome
        self.tempo_total = tempo_total
        self.tempo_restante = tempo_total
        self.tempo_conclusao = 0


def cadastrar_processos():
    fila = ListaCircularDupla()
    processos = []

    print("=== Cadastro de processos críticos ===")

    while True:
        entrada = input("Quantidade de processos: ")
        if entrada.isdigit() and int(entrada) > 0:
            qtd = int(entrada)
            break
        print("Digite um número válido.")

    for i in range(1, qtd + 1):
        print(f"\nProcesso {i}")

        nome = input("Nome: ").strip()
        while not nome:
            nome = input("Nome não pode ser vazio: ")

        while True:
            tempo = input("Tempo total (u.t.): ")
            if tempo.isdigit() and int(tempo) > 0:
                tempo = int(tempo)
                break
            print("Digite um número válido.")

        p = Processo(f"{i:02d}", nome, tempo)
        fila.inserir_final(p)
        processos.append(p)

    return fila, processos


def simular_round_robin(fila, quantum):
    historico = []
    tempo_atual = 0
    atual = fila.inicio

    while fila.tamanho > 0:
        processo = atual.dado

        tempo_exec = min(quantum, processo.tempo_restante)
        inicio = tempo_atual

        processo.tempo_restante -= tempo_exec
        tempo_atual += tempo_exec

        historico.append({
            "inicio": inicio,
            "nome": processo.nome,
            "executado": tempo_exec,
            "restante": processo.tempo_restante,
            "concluido": processo.tempo_restante == 0
        })

        proximo = atual.prox

        if processo.tempo_restante == 0:
            processo.tempo_conclusao = tempo_atual
            fila.remover_no(atual)

            if fila.tamanho == 0:
                break

            atual = proximo
        else:
            atual = atual.prox

    return historico


def exibir_historico(historico):
    print("\n=== Execução ===")
    for h in historico:
        linha = f"t={h['inicio']} -> {h['nome']} executa {h['executado']}u"
        if h["concluido"]:
            linha += " | CONCLUÍDO"
        else:
            linha += f" | restam {h['restante']}u"
        print(linha)


def exibir_relatorio(processos):
    print("\n=== RELATÓRIO FINAL ===")

    soma_espera = 0
    soma_retorno = 0

    print(f"{'Processo':15} {'Total':>6} {'Espera':>8} {'Retorno':>9}")

    for p in processos:
        espera = p.tempo_conclusao - p.tempo_total
        retorno = p.tempo_conclusao

        soma_espera += espera
        soma_retorno += retorno

        print(f"{p.nome:15} {p.tempo_total:>6} {espera:>8} {retorno:>9}")

    n = len(processos)
    print("\nMédia Espera :", round(soma_espera / n, 2))
    print("Média Retorno:", round(soma_retorno / n, 2))


def main():
    print("=== ARIA - Simulador Round Robin ===")

    fila, processos = cadastrar_processos()

    while True:
        q = input("\nQuantum: ")
        if q.isdigit() and int(q) > 0:
            quantum = int(q)
            break
        print("Digite um valor válido.")

    historico = simular_round_robin(fila, quantum)

    exibir_historico(historico)
    exibir_relatorio(processos)


if __name__ == "__main__":
    main()