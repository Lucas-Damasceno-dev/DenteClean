from clinic import Clinica
from dentist import Dentista
from patient import Paciente
from reception import Recepcao


def adicionar_novo_paciente():
    print("\n=== Adicionar Novo Paciente ===")
    paciente_nome = input("Digite o nome do paciente: ")
    paciente_idade = int(input("Digite a idade do paciente: "))
    paciente_rg = input("Digite o RG do paciente: ")
    paciente_endereco = input("Digite o endereço do paciente: ")
    paciente_telefone = input("Digite o telefone do paciente: ")
    novo_paciente = Paciente(paciente_nome, paciente_idade, paciente_rg, paciente_endereco, paciente_telefone)
    novo_paciente.adicionar_paciente(novo_paciente)


def marcar_horario_paciente(recepcao):
    id_paciente = int(input("Digite o ID do paciente: "))
    data_sessao = input("Digite a data da sessão (no formato YYYY-MM-DD): ")
    horario_sessao = input("Digite o horário da sessão (no formato HH:MM): ")

    paciente = next((p for p in recepcao.lista_espera if p["id"] == id_paciente), None)
    sessao_clinica = next((s for s in recepcao.lista_sessoes_clinicas if
                           s["data"] == data_sessao and s["horario"] == horario_sessao), None)

    if paciente and sessao_clinica:
        # Chame o método correto do dentista associado à recepção
        recepcao.dentista_associado.marcar_horario_paciente(paciente, sessao_clinica)
    else:
        print("Paciente ou sessão clínica não encontrados.")


def listar_horarios_marcados_paciente(recepcao):
    id_paciente = int(input("Digite o ID do paciente: "))

    paciente = next((p for p in recepcao.lista_espera if p["id"] == id_paciente), None)

    if paciente:
        recepcao.dentista_associado.listar_horarios_marcados_paciente(paciente)
    else:
        print("Paciente não encontrado.")


def confirmar_horario_paciente(recepcao):
    id_paciente = int(input("Digite o ID do paciente: "))

    paciente = next((p for p in recepcao.lista_espera if p["id"] == id_paciente), None)

    if paciente:
        # Chame o método correto do dentista associado à recepção
        recepcao.dentista_associado.confirmar_horario_paciente(paciente)
    else:
        print("Paciente não encontrado.")


def colocar_paciente_na_fila(recepcao):
    id_paciente = int(input("Digite o ID do paciente: "))
    paciente = next((p for p in recepcao.lista_espera if p["id"] == id_paciente), None)
    if paciente:
        recepcao.dentista_associado.colocar_paciente_na_fila(paciente)
    else:
        print("Paciente não encontrado.")


def menu_paciente():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    rg = input("Digite seu RG: ")
    endereco = input("Digite seu endereço: ")
    telefone = input("Digite seu telefone: ")

    paciente = Paciente(nome, idade, rg, endereco, telefone)
    lista_pacientes = []
    paciente.adicionar_paciente(lista_pacientes)

    while True:
        print("\n=== Menu do Paciente ===")
        print("1. Visualizar suas informações")
        print("2. Editar suas informações")
        print("3. Excluir seu cadastro")
        print("4. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_paciente = int(input("Digite o ID do paciente: "))
            paciente.visualizar_paciente(id_paciente, lista_pacientes)
        elif opcao == "2":
            id_paciente = int(input("Digite o ID do paciente: "))
            paciente.editar_paciente(id_paciente, lista_pacientes)
        elif opcao == "3":
            id_paciente = int(input("Digite o ID do paciente: "))
            paciente.excluir_paciente(id_paciente, lista_pacientes)
            break
        elif opcao == "4":
            break
        else:
            print("\nOpção inválida. Tente novamente.")


def menu_dentista():
    dentista = Dentista(input("Digite seu nome: "),
                        input("Digite seu horário de trabalho: "))

    while True:
        print("\n=== Menu do Dentista ===")
        print("1. Visualizar sua agenda")
        print("2. Adicionar observação a um paciente")
        print("3. Listar pacientes atendidos")
        print("4. Localizar sessão clínica")
        print("5. Iniciar sessão clínica")
        print("6. Atender próximo paciente")
        print("7. Ler prontuário completo de um paciente")
        print("8. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_dentista = int(input("Digite o ID do dentista: "))
            dentista.visualizar_agenda_dentista(id_dentista)
        elif opcao == "2":
            id_paciente = int(input("Digite o ID do paciente: "))
            observacao = input("Digite a observação a ser adicionada: ")
            dentista.adicionar_observacao_paciente(id_paciente, observacao)
        elif opcao == "3":
            dentista.listar_pacientes_atendidos()
        elif opcao == "4":
            data_sessao = input("Digite a data da sessão clínica (no formato YYYY-MM-DD): ")
            horario_sessao = input("Digite o horário da sessão clínica (no formato HH:MM): ")
            dentista.localizar_sessao_clinica(data_sessao, horario_sessao)
        elif opcao == "5":
            dentista.iniciar_sessao_clinica_dentista()
        elif opcao == "6":
            dentista.atender_proximo_paciente()
        elif opcao == "7":
            id_paciente = int(input("Digite o ID do paciente: "))
            dentista.ler_prontuario_completo_paciente(id_paciente)
        elif opcao == "8":
            break
        else:
            print("\nOpção inválida. Tente novamente.")


def menu_clinica():
    clinica = Clinica(input("Digite o nome da clínica: "),
                      input("Digite o endereço da clínica: "),
                      input("Digite o telefone da clínica: "))

    while True:
        print("\n=== Menu da Clínica ===")
        print("1. Adicionar dentista à clínica")
        print("2. Remover dentista da clínica")
        print("3. Visualizar dentistas na clínica")
        print("4. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dentista_nome = input("Digite o nome do dentista: ")
            dentista_horario = input("Digite o horário de trabalho do dentista: ")
            dentista = Dentista(dentista_nome, dentista_horario)
            clinica.adicionar_dentista(dentista)
        elif opcao == "2":
            id_dentista = int(input("Digite o ID do dentista a ser removido: "))
            clinica.remover_dentista(id_dentista)
        elif opcao == "3":
            clinica.visualizar_dentistas()
        elif opcao == "4":
            break
        else:
            print("\nOpção inválida. Tente novamente.")


def menu_recepcao():
    recepcao = Recepcao(input("Digite o horário de expediente da recepção: "))

    while True:
        print("\n=== Menu da Recepção ===")
        print("1. Adicionar dentista à recepção")
        print("2. Remover dentista da recepção")
        print("3. Visualizar dentistas no sistema")
        print("4. Adicionar sessão clínica")
        print("5. Listar sessões clínicas")
        print("6. Buscar sessão clínica")
        print("7. Iniciar sessão clínica a partir da recepção")
        print("8. Adicionar novo paciente")
        print("9. Marcar horário para paciente")
        print("10. Listar horários marcados para paciente")
        print("11. Confirmar horário para paciente na sessão atual")
        print("12. Colocar paciente em espera")
        print("13. Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            dentista_nome = input("Digite o nome do dentista: ")
            dentista_horario = input("Digite o horário de trabalho do dentista: ")
            dentista = Dentista(dentista_nome, dentista_horario)
            recepcao.adicionar_dentista(dentista)
        elif opcao == "2":
            id_dentista = int(input("Digite o ID do dentista a ser removido: "))
            recepcao.remover_dentista(id_dentista)
        elif opcao == "3":
            recepcao.visualizar_dentistas()
        elif opcao == "4":
            print("\n=== Adicionar Sessão Clínica ===")
            sessao_clinica_data = input("Digite a data da sessão clínica (no formato YYYY-MM-DD): ")
            sessao_clinica_horario = input("Digite o horário da sessão clínica (no formato HH:MM): ")
            sessao_clinica_duracao = input("Digite a duração da sessão clínica (em minutos): ")
            sessao_clinica_outros_dados = input("Digite outros dados opcionais da sessão clínica: ")
            recepcao.adicionar_sessao_clinica(sessao_clinica_data, sessao_clinica_horario, sessao_clinica_duracao,
                                              sessao_clinica_outros_dados)
        elif opcao == "5":
            recepcao.listar_sessoes_clinicas()
        elif opcao == "6":
            data_sessao = input("Digite a data da sessão clínica (no formato YYYY-MM-DD): ")
            horario_sessao = input("Digite o horário da sessão clínica (no formato HH:MM): ")
            recepcao.buscar_sessao_clinica(data_sessao, horario_sessao)
        elif opcao == "7":
            recepcao.iniciar_sessao_clinica_recepcao()
        elif opcao == "8":
            adicionar_novo_paciente()
        elif opcao == "9":
            marcar_horario_paciente(recepcao)
        elif opcao == "10":
            listar_horarios_marcados_paciente(recepcao)
        elif opcao == "11":
            confirmar_horario_paciente(recepcao)
        elif opcao == "12":
            colocar_paciente_na_fila(recepcao)
        elif opcao == "13":
            break
        else:
            print("\nOpção inválida. Tente novamente.")


# Menu principal
while True:
    print("\n=== Menu Principal ===")
    print("1. Sou um Paciente")
    print("2. Sou um Dentista")
    print("3. Sou uma Clínica")
    print("4. Sou uma Recepção")
    print("5. Sair")

    tipo_usuario = input("Escolha uma opção: ")

    if tipo_usuario == "1":
        menu_paciente()
    elif tipo_usuario == "2":
        menu_dentista()
    elif tipo_usuario == "3":
        menu_clinica()
    elif tipo_usuario == "4":
        menu_recepcao()
    elif tipo_usuario == "5":
        print("\nEncerrando o programa. Até logo!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
