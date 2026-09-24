from lenguajes import (
    prefijos,
    sufijos,
    subcadenas,
    cerradura_kleene,
    cerradura_positiva,
)


def test_cadena_vacia():
    assert prefijos("") == [""]
    assert sufijos("") == [""]
    assert subcadenas("") == [""]


def test_alfabeto_un_simbolo():
    assert cerradura_kleene(["a"], 3) == ["", "a", "aa", "aaa"]
    assert cerradura_positiva(["a"], 3) == ["a", "aa", "aaa"]


def test_prefijos_y_sufijos_longitud_uno():
    assert prefijos("a") == ["", "a"]
    assert sufijos("a") == ["a", ""]


def test_diferencia_kleene_positiva_longitud_cero():
    assert cerradura_kleene(["a", "b"], 0) == [""]
    assert cerradura_positiva(["a", "b"], 0) == []


def test_subcadenas():
    resultado = subcadenas("abc")

    assert "" in resultado
    assert "a" in resultado
    assert "b" in resultado
    assert "c" in resultado
    assert "ab" in resultado
    assert "bc" in resultado
    assert "abc" in resultado


def test_limite_de_200000_cadenas():
    try:
        cerradura_kleene(["a", "b"], 18)
        assert False
    except ValueError:
        assert True