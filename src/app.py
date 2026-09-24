import flet as ft

from lenguajes import (
    prefijos,
    sufijos,
    subcadenas,
    cerradura_kleene,
    cerradura_positiva,
)


def main(page: ft.Page):
    page.title = "Operaciones básicas sobre lenguajes"
    page.scroll = ft.ScrollMode.AUTO

    titulo = ft.Text(
        "Operaciones básicas sobre cadenas y lenguajes",
        size=24,
        weight=ft.FontWeight.BOLD,
    )

    # -------------------------------------------------
    # OPERACIÓN 1: PREFIJOS, SUFIJOS Y SUBCADENAS
    # -------------------------------------------------

    entrada_cadena = ft.TextField(
        label="Ingresa una cadena",
        hint_text="Ejemplo: abc",
    )

    resultado_cadena = ft.TextField(
        label="Resultados",
        multiline=True,
        read_only=True,
        min_lines=5,
        max_lines=12,
    )

    def mostrar_prefijos(e):
        resultado = prefijos(entrada_cadena.value)
        resultado_cadena.value = "Prefijos:\n" + "\n".join(
            "λ" if x == "" else x for x in resultado
        )
        page.update()

    def mostrar_sufijos(e):
        resultado = sufijos(entrada_cadena.value)
        resultado_cadena.value = "Sufijos:\n" + "\n".join(
            "λ" if x == "" else x for x in resultado
        )
        page.update()

    def mostrar_subcadenas(e):
        resultado = subcadenas(entrada_cadena.value)
        resultado_cadena.value = "Subcadenas:\n" + "\n".join(
            "λ" if x == "" else x for x in resultado
        )
        page.update()

    # -------------------------------------------------
    # OPERACIÓN 2: Σ* Y Σ+
    # -------------------------------------------------

    entrada_alfabeto = ft.TextField(
        label="Alfabeto",
        hint_text="Ejemplo: a,b",
    )

    entrada_longitud = ft.TextField(
        label="Longitud máxima",
        hint_text="Ejemplo: 3",
    )

    resultado_cerradura = ft.TextField(
        label="Resultados",
        multiline=True,
        read_only=True,
        min_lines=5,
        max_lines=12,
    )

    def obtener_datos():
        alfabeto = [
            simbolo.strip()
            for simbolo in entrada_alfabeto.value.split(",")
            if simbolo.strip()
        ]

        longitud = int(entrada_longitud.value)

        return alfabeto, longitud

    def mostrar_kleene(e):
        try:
            alfabeto, longitud = obtener_datos()
            resultado = cerradura_kleene(alfabeto, longitud)

            resultado_cerradura.value = "Σ*:\n" + ", ".join(
                "λ" if x == "" else x for x in resultado
            )

        except ValueError as error:
            resultado_cerradura.value = f"Error: {error}"

        page.update()

    def mostrar_positiva(e):
        try:
            alfabeto, longitud = obtener_datos()
            resultado = cerradura_positiva(alfabeto, longitud)

            resultado_cerradura.value = "Σ+:\n" + ", ".join(
                "λ" if x == "" else x for x in resultado
            )

        except ValueError as error:
            resultado_cerradura.value = f"Error: {error}"

        page.update()

    # -------------------------------------------------
    # GUARDAR RESULTADOS
    # -------------------------------------------------

    mensaje = ft.Text()

    def guardar_resultados(e):
        contenido = (
            "OPERACIONES SOBRE CADENAS\n\n"
            + resultado_cadena.value
            + "\n\nOPERACIONES SOBRE LENGUAJES\n\n"
            + resultado_cerradura.value
        )

        with open("resultados.txt", "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

        mensaje.value = "Resultados guardados en resultados.txt"
        page.update()

    # -------------------------------------------------
    # INTERFAZ
    # -------------------------------------------------

    page.add(
        titulo,

        ft.Divider(),

        ft.Text(
            "1. Prefijos, sufijos y subcadenas",
            size=20,
            weight=ft.FontWeight.BOLD,
        ),

        entrada_cadena,

        ft.Row(
            [
                ft.ElevatedButton(
                    "Prefijos",
                    on_click=mostrar_prefijos,
                ),
                ft.ElevatedButton(
                    "Sufijos",
                    on_click=mostrar_sufijos,
                ),
                ft.ElevatedButton(
                    "Subcadenas",
                    on_click=mostrar_subcadenas,
                ),
            ]
        ),

        resultado_cadena,

        ft.Divider(),

        ft.Text(
            "2. Cerraduras de lenguajes",
            size=20,
            weight=ft.FontWeight.BOLD,
        ),

        entrada_alfabeto,
        entrada_longitud,

        ft.Row(
            [
                ft.ElevatedButton(
                    "Calcular Σ*",
                    on_click=mostrar_kleene,
                ),
                ft.ElevatedButton(
                    "Calcular Σ+",
                    on_click=mostrar_positiva,
                ),
            ]
        ),

        resultado_cerradura,

        ft.Divider(),

        ft.ElevatedButton(
            "Guardar resultados",
            on_click=guardar_resultados,
        ),

        mensaje,
    )


ft.run(main)