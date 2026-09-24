from itertools import product


def prefijos(cadena):
    """Devuelve todos los prefijos de una cadena, incluyendo la cadena vacía."""
    return [cadena[:i] for i in range(len(cadena) + 1)]


def sufijos(cadena):
    """Devuelve todos los sufijos de una cadena, incluyendo la cadena vacía."""
    return [cadena[i:] for i in range(len(cadena) + 1)]


def subcadenas(cadena):
    """Devuelve todas las subcadenas distintas, incluyendo la cadena vacía."""
    resultado = {""}

    for inicio in range(len(cadena)):
        for fin in range(inicio + 1, len(cadena) + 1):
            resultado.add(cadena[inicio:fin])

    return sorted(resultado, key=lambda x: (len(x), x))


def cerradura_kleene(alfabeto, longitud_maxima):
    """Calcula Σ* hasta la longitud máxima indicada."""
    if longitud_maxima < 0:
        raise ValueError("La longitud máxima no puede ser negativa.")

    cantidad = sum(
        len(alfabeto) ** n
        for n in range(longitud_maxima + 1)
    )

    if cantidad > 200000:
        raise ValueError(
            "La combinación generaría más de 200000 cadenas."
        )

    resultado = []

    for longitud in range(longitud_maxima + 1):
        for cadena in product(alfabeto, repeat=longitud):
            resultado.append("".join(cadena))

    return resultado


def cerradura_positiva(alfabeto, longitud_maxima):
    """Calcula Σ+ hasta la longitud máxima indicada."""
    if longitud_maxima < 0:
        raise ValueError("La longitud máxima no puede ser negativa.")

    if longitud_maxima == 0:
        return []

    cantidad = sum(
        len(alfabeto) ** n
        for n in range(1, longitud_maxima + 1)
    )

    if cantidad > 200000:
        raise ValueError(
            "La combinación generaría más de 200000 cadenas."
        )

    resultado = []

    for longitud in range(1, longitud_maxima + 1):
        for cadena in product(alfabeto, repeat=longitud):
            resultado.append("".join(cadena))

    return resultado