def simular_round_robin(rajadas, quantum, tempo_contexto):
    """
    Simula o algoritmo Round Robin.

    Retorna:
    - tempo de espera de cada processo
    - soma dos tempos de espera
    - tempo médio de espera
    - número de trocas de contexto
    - tempo total de overhead
    - tempo total de CPU usado nos processos
    """

    n = len(rajadas)

    # Tempo restante de cada processo
    restante = rajadas.copy()

    # Tempo de término de cada processo
    termino = [0] * n

    # Fila de processos
    fila = list(range(n))

    # Tempo total
    tempo = 0

    # Contador de trocas de contexto
    trocas_contexto = 0

    # ==============================
    # SIMULAÇÃO
    # ==============================

    while fila:

        # Pega o primeiro processo da fila
        i = fila.pop(0)

        # Executa pelo quantum ou até terminar
        execucao = min(restante[i], quantum)

        tempo += execucao
        restante[i] -= execucao

        # Processo terminou
        if restante[i] == 0:

            termino[i] = tempo

            # Se existem outros processos,
            # haverá troca para o próximo
            if fila:
                trocas_contexto += 1
                tempo += tempo_contexto

        # Processo ainda não terminou
        else:

            # Volta para o final da fila
            fila.append(i)

            # Troca de contexto para o próximo processo
            trocas_contexto += 1
            tempo += tempo_contexto

    # ==============================
    # TEMPOS DE ESPERA
    # ==============================

    espera = []

    for i in range(n):
        tempo_espera = termino[i] - rajadas[i]
        espera.append(tempo_espera)

    soma_espera = sum(espera)

    media_espera = soma_espera / n

    # ==============================
    # OVERHEAD
    # ==============================

    tempo_total_contexto = trocas_contexto * tempo_contexto

    # Tempo efetivamente utilizado pelos processos
    tempo_cpu_processos = sum(rajadas)

    # Percentual de overhead
    percentual_overhead = (
        tempo_total_contexto / tempo_cpu_processos
    ) * 100

    return (
        espera,
        soma_espera,
        media_espera,
        trocas_contexto,
        tempo_total_contexto,
        tempo_cpu_processos,
        percentual_overhead
    )


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

def round_robin():

    # ==============================
    # ENTRADA
    # ==============================

    n = int(input("Digite o número de processos: "))

    rajadas = []

    for i in range(n):
        rajada = float(
            input(f"Digite o tempo de rajada do P{i + 1} (ms): ")
        )
        rajadas.append(rajada)

    quantum = float(
        input("Digite o quantum (ms): ")
    )

    tempo_contexto = float(
        input("Digite o tempo de uma troca de contexto (ms): ")
    )

    # ==================================================
    # SIMULAÇÃO COM O QUANTUM INFORMADO
    # ==================================================

    resultado = simular_round_robin(
        rajadas,
        quantum,
        tempo_contexto
    )

    (
        espera,
        soma_espera,
        media_espera,
        trocas_contexto,
        tempo_total_contexto,
        tempo_cpu_processos,
        percentual_overhead
    ) = resultado

    # ==============================
    # RESULTADO PRINCIPAL
    # ==============================

    print("\n========================================")
    print("       RESULTADO - ROUND ROBIN")
    print("========================================")

    print(f"\nQuantum utilizado: {quantum:.2f} ms")

    print("\nTempo de espera de cada processo:")

    for i in range(n):
        print(
            f"P{i + 1}: {espera[i]:.2f} ms"
        )

    print("\n----------------------------------------")

    print(
        f"Soma dos tempos de espera: "
        f"{soma_espera:.2f} ms"
    )

    print(
        f"Tempo médio de espera: "
        f"{soma_espera:.2f} / {n} = "
        f"{media_espera:.2f} ms"
    )

    print("\n----------------------------------------")

    print(
        f"Total de trocas de contexto: "
        f"{trocas_contexto}"
    )

    print(
        f"Tempo de cada troca: "
        f"{tempo_contexto:.2f} ms"
    )

    # ==================================================
    # A) TEMPO TOTAL DE OVERHEAD
    # ==================================================

    print("\na) TEMPO TOTAL DE OVERHEAD")

    print(
        f"{trocas_contexto} × {tempo_contexto:.2f} = "
        f"{tempo_total_contexto:.2f} ms"
    )

    # ==================================================
    # B) PERCENTUAL DE OVERHEAD
    # ==================================================

    print("\nb) PERCENTUAL DE OVERHEAD")

    print(
        f"Tempo de CPU dos processos: "
        f"{tempo_cpu_processos:.2f} ms"
    )

    print(
        f"Tempo gasto em trocas: "
        f"{tempo_total_contexto:.2f} ms"
    )

    print(
        f"Overhead = "
        f"({tempo_total_contexto:.2f} / "
        f"{tempo_cpu_processos:.2f}) × 100"
    )

    print(
        f"Overhead = {percentual_overhead:.2f}%"
    )

    # ==================================================
    # C) IMPACTO DO QUANTUM = 10 ms
    # ==================================================

    quantum_10 = 10

    resultado_10 = simular_round_robin(
        rajadas,
        quantum_10,
        tempo_contexto
    )

    (
        espera_10,
        soma_espera_10,
        media_espera_10,
        trocas_10,
        overhead_10,
        cpu_10,
        percentual_10
    ) = resultado_10

    print("\n========================================")
    print("c) IMPACTO DO QUANTUM = 10 ms")
    print("========================================")

    print("\nCom quantum = 10 ms:")

    print(
        f"Tempo médio de espera: "
        f"{media_espera_10:.2f} ms"
    )

    print(
        f"Trocas de contexto: "
        f"{trocas_10}"
    )

    print(
        f"Overhead total: "
        f"{overhead_10:.2f} ms"
    )

    print(
        f"Percentual de overhead: "
        f"{percentual_10:.2f}%"
    )

    print("\n----------------------------------------")
    print("COMPARAÇÃO")
    print("----------------------------------------")

    print(
        f"Quantum atual ({quantum:.2f} ms):"
    )

    print(
        f"  Trocas: {trocas_contexto}"
    )

    print(
        f"  Tempo médio de espera: "
        f"{media_espera:.2f} ms"
    )

    print(
        f"  Overhead: "
        f"{tempo_total_contexto:.2f} ms"
    )

    print(
        f"  Overhead (%): "
        f"{percentual_overhead:.2f}%"
    )

    print("\nQuantum = 10 ms:")

    print(
        f"  Trocas: {trocas_10}"
    )

    print(
        f"  Tempo médio de espera: "
        f"{media_espera_10:.2f} ms"
    )

    print(
        f"  Overhead: "
        f"{overhead_10:.2f} ms"
    )

    print(
        f"  Overhead (%): "
        f"{percentual_10:.2f}%"
    )

    # ==================================================
    # ANÁLISE AUTOMÁTICA
    # ==================================================

    print("\n========================================")
    print("ANÁLISE DO IMPACTO")
    print("========================================")

    if trocas_10 < trocas_contexto:
        print(
            f"\nCom quantum = 10 ms, o número de "
            f"trocas diminuiu de {trocas_contexto} "
            f"para {trocas_10}."
        )

        print(
            "Isso reduz o overhead causado pelas "
            "trocas de contexto."
        )

    elif trocas_10 > trocas_contexto:
        print(
            f"\nCom quantum = 10 ms, o número de "
            f"trocas aumentou de {trocas_contexto} "
            f"para {trocas_10}."
        )

    else:
        print(
            "\nO número de trocas de contexto "
            "permaneceu igual."
        )

    if media_espera_10 < media_espera:
        print(
            f"\nO tempo médio de espera diminuiu "
            f"de {media_espera:.2f} ms para "
            f"{media_espera_10:.2f} ms."
        )

    elif media_espera_10 > media_espera:
        print(
            f"\nO tempo médio de espera aumentou "
            f"de {media_espera:.2f} ms para "
            f"{media_espera_10:.2f} ms."
        )

    else:
        print(
            "\nO tempo médio de espera permaneceu igual."
        )

    print("\n========================================")


# Executar o programa
round_robin()
