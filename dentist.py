from datetime import datetime


class Dentista:
    def __init__(self, nome, horario_trabalho):
        self.nome = nome
        self.horario_trabalho = horario_trabalho
        self.pacientes_atendidos = []

    def visualizar_agenda_dentista(self, id_dentista):
        print(f"Agenda do Dentista {self.nome} (ID: {id_dentista}):")
        print(f"Horário de Trabalho: {self.horario_trabalho}")
        print(f"Pacientes Atendidos: {', '.join([str(p) for p in self.pacientes_atendidos])}")

    def adicionar_observacao_paciente(self, id_paciente, observacao):
        paciente = next((p for p in self.pacientes_atendidos if p["id"] == id_paciente), None)
        if paciente:
            if "observacoes" in paciente:
                paciente["observacoes"].append(observacao)
            else:
                paciente["observacoes"] = [observacao]
            print(f"Observação adicionada para o Paciente {paciente['nome']}.")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado na lista de pacientes atendidos.")

    def listar_pacientes_atendidos(self):
        print(f"Pacientes Atendidos pelo Dentista {self.nome}:")
        for paciente in self.pacientes_atendidos:
            print(f"ID: {paciente['id']}, Nome: {paciente['nome']}")

    def localizar_sessao_clinica(self, data, horario):
        data_horario = f"{data} {horario}"
        try:
            data_hora_sessao = datetime.strptime(data_horario, "%Y-%m-%d %H:%M")
            # Agora você tem um objeto datetime representando a data e hora da sessão clínica
            # Você pode usar essa informação para comparar com as sessões clínicas existentes
            # na agenda do dentista e tomar as ações apropriadas.
            print(f"Sessão clínica localizada para {data} às {horario}.")
        except ValueError:
            print("Formato de data ou horário inválido. Use o formato: YYYY-MM-DD HH:MM")

    def iniciar_sessao_clinica_dentista(self):
        if self.horario_trabalho:
            print(f"Iniciando a sessão clínica para o dentista {self.nome}.")
            print(f"Horário de trabalho: {self.horario_trabalho}")
            # Adicione aqui qualquer lógica adicional que você precisa ao iniciar uma sessão clínica.
        else:
            print("O dentista não possui um horário de trabalho definido.")

    def atender_proximo_paciente(self):
        if not self.pacientes_atendidos:
            print("Não há pacientes na agenda para atender.")
            return

        proximo_paciente = self.pacientes_atendidos.pop(0)
        print(f"Atendendo o próximo paciente: {proximo_paciente['nome']}")
        if 'observacoes' in proximo_paciente:
            for observacao in proximo_paciente['observacoes']:
                print(f"Observação: {observacao}")

    def ler_prontuario_completo_paciente(self, id_paciente):
        paciente = next((p for p in self.pacientes_atendidos if p["id"] == id_paciente), None)
        if paciente:
            print(f"Prontuário completo do Paciente {paciente['nome']}:")
            print(f"ID: {paciente['id']}")
            print(f"Nome: {paciente['nome']}")
            print(f"Idade: {paciente['idade']}")
            print(f"RG: {paciente['rg']}")
            print(f"Endereço: {paciente['endereco']}")
            print(f"Telefone: {paciente['telefone']}")
            if 'observacoes' in paciente:
                print("Observações:")
                for observacao in paciente['observacoes']:
                    print(f"  - {observacao}")
            else:
                print("Não há observações registradas para este paciente.")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado na lista de pacientes atendidos.")

    def ler_primeira_anotacao_paciente(self, id_paciente):
        paciente = next((p for p in self.pacientes_atendidos if p["id"] == id_paciente), None)
        if paciente:
            if 'observacoes' in paciente and paciente['observacoes']:
                primeira_anotacao = paciente['observacoes'][0]
                print(f"Primeira anotação do Paciente {paciente['nome']}:")
                print(f"  - {primeira_anotacao}")
            else:
                print(f"Não há anotações registradas para o paciente {paciente['nome']}.")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado na lista de pacientes atendidos.")

    def ler_ultima_anotacao_paciente(self, id_paciente):
        paciente = next((p for p in self.pacientes_atendidos if p["id"] == id_paciente), None)
        if paciente:
            if 'observacoes' in paciente and paciente['observacoes']:
                ultima_anotacao = paciente['observacoes'][-1]
                print(f"Última anotação do Paciente {paciente['nome']}:")
                print(f"  - {ultima_anotacao}")
            else:
                print(f"Não há anotações registradas para o paciente {paciente['nome']}.")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado na lista de pacientes atendidos.")

    def anotar_prontuario_paciente(self, id_paciente, anotacao):
        paciente = next((p for p in self.pacientes_atendidos if p["id"] == id_paciente), None)
        if paciente:
            if 'observacoes' in paciente:
                paciente['observacoes'].append(anotacao)
            else:
                paciente['observacoes'] = [anotacao]
            print(f"Anotação adicionada ao prontuário do Paciente {paciente['nome']}.")
        else:
            print(f"Paciente com ID {id_paciente} não encontrado na lista de pacientes atendidos.")
