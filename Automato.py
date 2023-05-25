class Automato:
    def __init__(automato, estados, alfabeto, transicoes, inicialestados, finalestados):
        automato.estados = estados
        automato.alfabeto = alfabeto
        automato.transicoes = transicoes
        automato.inicialestados = inicialestados
        automato.finalestados = finalestados

    def simulate(automato, input):
        atualestados = automato.epsilon_closure(automato.inicialestados)

        for symbol in input:
            nextestados = set()
            for estado in atualestados:
                if estado in automato.transicoes and symbol in automato.transicoes[estado]:
                    estadosWithSymbol = automato.transicoes[estado][symbol]
                    nextestados.update(estadosWithSymbol)
            atualestados = automato.epsilon_closure(nextestados)

        return any(estado in automato.finalestados for estado in atualestados)

    def epsilon_closure(automato, estados):
        pilha = list(estados)
        closure = set(estados)

        while pilha:
            estado = pilha.pop()
            epsilonestados = automato.transicoes.get(estado, {}).get('', set())
            for epsilonestado in epsilonestados:
                if epsilonestado not in closure:
                    closure.add(epsilonestado)
                    pilha.append(epsilonestado)

        return closure


def main():
    estados = {0, 1, 2, 3}
    alfabeto = {'0', '1'}
    transicoes = {
        0: {'0': {0}, '1': {0, 1}},
        1: {'1': {2}},
        2: {'0': {3}, '1': {3}},
        3: {'0': {3}, '1': {3}}
    }

    # q0 -> 0 -> q0
    # q0 -> 1 -> q0 e q1

    # q1 -> 1 -> q2

    # q2 -> 0 -> q3
    # q2 -> 1 ->q3

    # q3 -> 0 ->q3
    # q3 -> 1 ->q3

    inicialestados = {0}
    finalestados = {3}

    automato = Automato(estados, alfabeto, transicoes,
                        inicialestados, finalestados)

    # Caso professor solicitar, colocar input pelo terminal mesmo
    lista = ["0011", "01101000111011"]

    for lista in lista:
        accepted = automato.simulate(lista)
        result = "ACEITO" if accepted else "REJEITADO"
        print(f"Comandos: {lista}, Resposta: {result}")


if __name__ == "__main__":
    main()
