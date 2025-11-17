items = []
n = 0
i = 0
j = None


def init(vals):

    global items, n, i, j
    items = list(vals)     # Se copia la lista para trabajar sobre una nueva instancia
    n = len(items)         # Se guarda la cantidad de elementos
    i = 1                  # i comienza desde el segundo elemento
    j = None               # j se usará cuando se inicie el desplazamiento del elemento i


def step():

    global items, n, i, j

    # Si i alcanzó el tamaño de la lista, el algoritmo terminó
    if i >= n:
        return {"done": True}

    # Si se comienza a procesar un nuevo elemento i
    if j is None:
        j = i  # Se inicializa j en la posición actual de i
        # Se indica comparación sin intercambio
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # desplaza el elemento hacia la izquierda mientras sea menor que su predecesor
    while j > 0 and items[j-1] > items[j]:

        # Se realiza el intercambio entre posiciones adyacentes
        items[j-1], items[j] = items[j], items[j-1]

        # j retrocede una posición
        j -= 1

        # Se devuelve esta operación individual para animación paso a paso
        return {"a": j, "b": j+1, "swap": True, "done": False}

    # Si ya no es necesario desplazar más, se avanza al siguiente i
    i += 1
    j = None  # Se reinicia j para la próxima iteración

    # Se devuelve un paso sin intercambio
    return {"swap": False, "done": False}
