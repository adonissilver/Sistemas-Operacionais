def tempo_medio_espera():

    # Número de processos
    n = int(input("Digite o número de processos: "))

    # Tempos de rajada
    rajadas = []

    for i in range(n):
        rajada = int(input(f"Digite o tempo de rajada do P{i + 1}: "))
        rajadas.append(rajada)

    # Quantum
    quantum = int(input("Digite o quantum: "))

    # Cópia das rajadas para controlar o tempo restante
    restante = rajadas.copy()

    # Guarda o tempo de término de cada processo
    termino = [0] * n

    # Fila inicial
    fila = list(range(n))

    # Tempo atual da CPU
    tempo = 0

    # Simulação do Round Robin
    while fila:

        # Retira o primeiro processo da fila
        i = fila.pop(0)

        # Executa pelo quantum ou até terminar
        execucao = min(restante[i], quantum)

        tempo += execucao
        restante[i] -= execucao

        # Se o processo terminou
        if restante[i] == 0:
            termino[i] = tempo

        # Caso contrário, volta para o final da fila
        else:
            fila.append(i)

    # Calcula o tempo de espera de cada processo
    espera = []

    for i in range(n):
        tempo_espera = termino[i] - rajadas[i]
        espera.append(tempo_espera)

    # Soma dos tempos de espera
    soma_espera = sum(espera)

    # Tempo médio de espera
    media = soma_espera / n

    # Exibe os resultados
    print("\n==============================")
    print("       RESULTADO")
    print("==============================")

    for i in range(n):
        print(f"Tempo de espera do P{i + 1}: {espera[i]}")

    print("------------------------------")
    print(f"Soma dos tempos de espera: {soma_espera}")
    print(f"Quantidade de processos: {n}")
    print(f"Tempo médio de espera: {soma_espera} / {n} = {media:.2f}")
    print("==============================")


# Executa o programa
tempo_medio_espera()