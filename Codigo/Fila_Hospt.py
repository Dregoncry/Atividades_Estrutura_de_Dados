from LDPE import Lista_Duplamente_Encadeada


class Paciente:
	def __init__(self, nome, prioritario):
		self.nome = nome
		self.prioritario = prioritario


class Fila_Hospital:
	def __init__(self):
		self.lista = Lista_Duplamente_Encadeada()
		self.qtd_prioritarios = 0

	def inserir(self, nome, prioritario):
		paciente = Paciente(nome, prioritario)

		if prioritario:
			self.lista.inserir_posicao(paciente, self.qtd_prioritarios)
			self.qtd_prioritarios += 1
		else:
			self.lista.inserir_final(paciente)

	def atender(self):
		if self.lista.tamanho == 0:
			return None

		paciente = self.lista.inicio.dado
		self.lista.remover(paciente)

		if paciente.prioritario:
			self.qtd_prioritarios -= 1

		return paciente

	def exibir(self):
		if self.lista.tamanho == 0:
			print("Fila vazia")
			return

		aux = self.lista.inicio
		indice = 0
		while aux is not None:
			tipo = "PRIORITARIO" if aux.dado.prioritario else "COMUM"
			print(f"{indice} - {aux.dado.nome} ({tipo})")
			aux = aux.dir
			indice += 1

	def buscar(self, nome):
		aux = self.lista.inicio
		indice = 0
		while aux is not None:
			if aux.dado.nome.lower() == nome.lower():
				tipo = "PRIORITARIO" if aux.dado.prioritario else "COMUM"
				print(f"Paciente encontrado na posicao {indice}: {aux.dado.nome} ({tipo})")
				return
			aux = aux.dir
			indice += 1

		print(f"Paciente '{nome}' nao encontrado na fila.")


def main():
	fila = Fila_Hospital()

	while True:
		print()
		print("===== FILA DO HOSPITAL CENTRAL =====")
		print("1. Inserir paciente")
		print("2. Atender proximo paciente")
		print("3. Exibir fila")
		print("4. Buscar paciente")
		print("0. Sair")

		opcao = input("Escolha uma opcao: ").strip()

		match opcao:
			case "1":
				nome = input("Nome do paciente: ").strip()
				while not nome:
					print("Nome nao pode ser vazio.")
					nome = input("Nome do paciente: ").strip()

				tipo = input("Caso prioritario? (s/n): ").strip().lower()
				while tipo not in ("s", "n"):
					print("Digite s para sim ou n para nao.")
					tipo = input("Caso prioritario? (s/n): ").strip().lower()

				fila.inserir(nome, tipo == "s")
				print(f"Paciente '{nome}' inserido na fila.")

			case "2":
				paciente = fila.atender()
				if paciente is None:
					print("Fila vazia. Nenhum paciente para atender.")
				else:
					tipo = "prioritario" if paciente.prioritario else "comum"
					print(f"Atendendo: {paciente.nome} ({tipo})")

			case "3":
				fila.exibir()

			case "4":
				nome = input("Nome do paciente: ").strip()
				fila.buscar(nome)

			case "0":
				print("Encerrando o sistema.")
				break

			case _:
				print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
	main()
