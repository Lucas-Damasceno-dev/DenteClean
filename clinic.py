class Clinica:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.lista_dentistas = []
        self.prontuario_dos_pacientes = []

    def adicionar_dentista(self, dentista):
        self.lista_dentistas.append(dentista)
        print(f"Dentista {dentista.nome} adicionado à clínica {self.nome}.")

    def remover_dentista(self, id_dentista):
        dentista = next((d for d in self.lista_dentistas if d.id == id_dentista), None)
        if dentista:
            self.lista_dentistas.remove(dentista)
            print(f"Dentista {dentista.nome} removido da clínica {self.nome}.")
        else:
            print(f"Dentista com ID {id_dentista} não encontrado na clínica {self.nome}.")

    def visualizar_dentistas(self):
        print(f"Dentistas na clínica {self.nome}:")
        for idx, dentista in enumerate(self.lista_dentistas):
            print(f"ID: {idx + 1}, Nome: {dentista.nome}")
