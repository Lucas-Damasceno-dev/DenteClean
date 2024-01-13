class Paciente:
    def __init__(self, nome, idade, rg, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.endereco = endereco
        self.telefone = telefone

    def adicionar_paciente(self, lista_pacientes):
        novo_id = len(lista_pacientes) + 1
        paciente = {
            "id": novo_id,
            "nome": self.nome,
            "idade": self.idade,
            "rg": self.rg,
            "endereco": self.endereco,
            "telefone": self.telefone
        }
        lista_pacientes.append(paciente)
        print(f"Paciente {self.nome} adicionado com sucesso!")

    @staticmethod
    def visualizar_paciente(id_paciente, lista_pacientes):
        paciente = next((p for p in lista_pacientes if p["id"] == id_paciente), None)
        if paciente:
            print(f"Informações do Paciente {paciente['nome']}:")
            print(f"ID: {paciente['id']}")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"RG: {paciente['rg']}")
            print(f"Endereço: {paciente['endereco']}")
            print(f"Telefone: {paciente['telefone']}")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado.")

    def editar_paciente(self, id_paciente, lista_pacientes):
        paciente = next((p for p in lista_pacientes if p["id"] == id_paciente), None)
        if paciente:
            novo_nome = input(f"Digite o novo nome para o paciente {paciente['nome']}: ")
            novo_idade = int(input(f"Digite a nova idade para o paciente {paciente['nome']}: "))
            novo_rg = input(f"Digite o novo RG para o paciente {paciente['nome']}: ")
            novo_endereco = input(f"Digite o novo endereço para o paciente {paciente['nome']}: ")
            novo_telefone = input(f"Digite o novo telefone para o paciente {paciente['nome']}: ")

            # Atualizando os dados do paciente
            paciente.update({
                "nome": novo_nome,
                "idade": novo_idade,
                "rg": novo_rg,
                "endereco": novo_endereco,
                "telefone": novo_telefone
            })

            print(f"Informações do Paciente {paciente['nome']} atualizadas com sucesso!")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado.")

    @staticmethod
    def excluir_paciente(id_paciente, lista_pacientes):
        paciente = next((p for p in lista_pacientes if p["id"] == id_paciente), None)
        if paciente:
            lista_pacientes.remove(paciente)
            print(f"Paciente {paciente['nome']} removido com sucesso!")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado.")
