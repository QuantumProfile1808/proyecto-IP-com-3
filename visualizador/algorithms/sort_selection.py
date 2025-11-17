# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase

    if i >= n - 1:    #cuando i llega al final no ordenado, se termina
        return {"done": True} 

    # ---- FASE BUSCAR ----
    if fase == "buscar":
        # Mientras j esté dentro de la lista seguimos comparando
        if j < n:
            a = min_idx
            b = j       # índice del elemento que estamos comparando ahora
            
            if items[j] < items[min_idx]: # actualizar mínimo si corresponde
                min_idx = j

            j += 1   
            return {"a": a, "b": b, "swap": False, "done": False}

        # terminó el barrido → pasar a fase swap
        fase = "swap"
        return {"a": min_idx, "b": i, "swap": False, "done": False}

    # ---- FASE SWAP ----
    if fase == "swap":
        if min_idx != i:   # Si el mínimo encontrado no está donde debería, lo intercambiamos
            
            items[i], items[min_idx] = items[min_idx], items[i]
            a = i
            b = min_idx
        else:    # Si min_idx == i, no hay cambio: el mínimo ya está en su lugar
            a = i
            b = i

        # mover a la próxima iteración
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"

        return {"a": a, "b": b, "swap": (a != b), "done": False}
