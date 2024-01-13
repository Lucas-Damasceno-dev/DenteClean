class Recepcao:
    def __init__(self, horario_expediente):
        self.horario_expediente = horario_expediente
        self.lista_espera = []
        self.lista_dentistas = []
        self.lista_sessoes_clinicas = []
        self.dentista_associado = None  # Inicialmente, nenhum dentista associado

    def adicionar_dentista_associado(self, dentista):
        self.dentista_associado = dentista

    def adicionar_dentista(self, dentista):
        self.lista_dentistas.append(dentista)
        print(f"Dentista {dentista.nome} adicionado ao sistema.")

    def remover_dentista(self, id_dentista):
        dentista = next((d for d in self.lista_dentistas if d.id == id_dentista), None)
        if dentista:
            self.lista_dentistas.remove(dentista)
            print(f"Dentista {dentista.nome} removido do sistema.")
        else:
            print(f"Dentista com ID {id_dentista} não encontrado no sistema.")

    def visualizar_dentistas(self):
        print("Dentistas no sistema:")
        for dentista in self.lista_dentistas:
            print(f"ID: {dentista.id}, Nome: {dentista.nome}")

    def adicionar_sessao_clinica(self, data, horario, duracao, outros_dados_opcionais):
        sessao_clinica = {
            "data": data,
            "horario": horario,
            "duracao": duracao,
            "outros_dados_opcionais": outros_dados_opcionais
        }
        self.lista_sessoes_clinicas.append(sessao_clinica)
        print(f"Sessão clínica adicionada para {data} às {horario}.")

    def listar_sessoes_clinicas(self):
        print("Lista de todas as sessões clínicas:")
        for sessao_clinica in self.lista_sessoes_clinicas:
            print(f"Data: {sessao_clinica['data']}, Horário: {sessao_clinica['horario']}, "
                  f"Duracao: {sessao_clinica['duracao']}, Outros Dados: {sessao_clinica['outros_dados_opcionais']}")

    def buscar_sessao_clinica(self, data, horario):
        sessao_clinica = next((s for s in self.lista_sessoes_clinicas
                               if s['data'] == data and s['horario'] == horario), None)
        if sessao_clinica:
            print(f"Sessão clínica encontrada para {data} às {horario}.")
            print(f"Duracao: {sessao_clinica['duracao']}, Outros Dados: {sessao_clinica['outros_dados_opcionais']}")
        else:
            print(f"Sessão clínica não encontrada para {data} às {horario}.")

    def iniciar_sessao_clinica_recepcao(self):
        if self.lista_sessoes_clinicas:
            sessao_clinica = self.lista_sessoes_clinicas[0]
            print(f"Iniciando sessão clínica a partir da recepção para"
                  f" {sessao_clinica['data']} às {sessao_clinica['horario']}.")
            # Adicione aqui qualquer lógica adicional que você precisa ao iniciar uma sessão clínica.
        else:
            print("Não há sessões clínicas disponíveis para iniciar.")

    def adicionar_novo_paciente(self, identidade, nome, outros_dados_pessoais):
        paciente = {
            "identidade": identidade,
            "nome": nome,
            "outros_dados_pessoais": outros_dados_pessoais
        }
        self.lista_espera.append(paciente)
        print(f"Paciente {nome} adicionado ao sistema.")

    def marcar_horario_para_paciente(self, paciente, sessao_clinica):
        if sessao_clinica in self.lista_sessoes_clinicas:
            horario = f"{sessao_clinica['data']} às {sessao_clinica['horario']}"
            print(f"Marcando horário para o paciente {paciente['nome']} na sessão clínica de {horario}.")
            # Adicione aqui qualquer lógica adicional que você precisa para marcar o horário.
        else:
            print("Sessão clínica não encontrada. Não é possível marcar o horário para o paciente.")

    def listar_horarios_marcados_paciente(self, paciente):
        if paciente in self.lista_espera:
            print(f"Horários marcados para o paciente {paciente['nome']}:")
            # Adicione aqui a lógica para listar os horários marcados para o paciente.
        else:
            print(f"Paciente {paciente['nome']} não encontrado na lista de espera.")

    def confirmar_horario_paciente_sessao_atual(self, paciente):
        if self.lista_espera:
            paciente_na_frente = self.lista_espera[0]
            if paciente_na_frente == paciente:
                print(f"Horário confirmado para o paciente {paciente['nome']} na sessão atual.")
                # Adicione aqui qualquer lógica adicional que você precisa para confirmar o horário.
            else:
                print(f"O paciente {paciente['nome']} não está na frente da fila. Não é possível confirmar o horário.")
        else:
            print("A fila de espera está vazia.")

    def colocar_paciente_na_fila(self, paciente):
        self.lista_espera.append(paciente)
        print(f"Paciente {paciente.nome} colocado na fila de espera.")

    def listar_proximo_paciente_fila_atendimento(self):
        if self.lista_espera:
            proximo_paciente = self.lista_espera.pop(0)
            print(f"Próximo paciente na fila de espera: {proximo_paciente.nome}")
        else:
            print("A fila de espera está vazia.")

    def listar_consultas_realizadas_sessao_clinica(self, sessao_clinica):
        if sessao_clinica in self.lista_sessoes_clinicas:
            print(f"Consultas realizadas na sessão clínica de {sessao_clinica['data']} às {sessao_clinica['horario']}:")

            if 'consultas_realizadas' in sessao_clinica:
                for consulta in sessao_clinica['consultas_realizadas']:
                    print(f"- Paciente: {consulta['paciente']}, Dentista: {consulta['dentista']},"
                          f" Data: {consulta['data']}, Horário: {consulta['horario']}")
            else:
                print("Nenhuma consulta realizada nesta sessão clínica.")

        else:
            print("Sessão clínica não encontrada. Não é possível listar as consultas realizadas.")
