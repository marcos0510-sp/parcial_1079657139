import re

VOWELS = set("aeiouAEIOU")


def contar_caracteres(texto: str) -> int:
    """Cuenta todos los caracteres del texto (incluyendo espacios)."""
    return len(texto)


def contar_palabras(texto: str) -> int:
    """Cuenta palabras según separación por espacios en blanco."""
    palabras = re.findall(r"\b\w+\b", texto)
    return len(palabras)


def contar_oraciones(texto: str) -> int:
    """Cuenta oraciones separadas por '.', '!' o '?' (ignora segmentos vacíos)."""
    partes = re.split(r"[.!?]+", texto)
    oraciones = [p for p in (p.strip() for p in partes) if p]
    return len(oraciones)


def palabra_mas_larga(texto: str) -> str:
    """Devuelve la palabra más larga en el texto."""
    palabras = re.findall(r"\b\w+\b", texto)
    return max(palabras, key=len) if palabras else ""


def palabra_mas_corta(texto: str) -> str:
    """Devuelve la palabra más corta en el texto."""
    palabras = re.findall(r"\b\w+\b", texto)
    return min(palabras, key=len) if palabras else ""


def contar_vocales(texto: str) -> int:
    """Cuenta el número de vocales (mayúsculas y minúsculas)."""
    return sum(1 for c in texto if c in VOWELS)


def contar_consonantes(texto: str) -> int:
    """Cuenta el número de consonantes (letras que no son vocales)."""
    return sum(1 for c in texto if c.isalpha() and c not in VOWELS)


def main():
    while True:
        texto = input("Ingrese un texto para analizar: ").strip()
        if texto:
            break
        print("El texto no puede estar vacío. Intente de nuevo.")

    caracteres = contar_caracteres(texto)
    palabras = contar_palabras(texto)
    oraciones = contar_oraciones(texto)
    mas_larga = palabra_mas_larga(texto)
    mas_corta = palabra_mas_corta(texto)
    vocales = contar_vocales(texto)
    consonantes = contar_consonantes(texto)

    print("\n=== Estadísticas del texto ===")
    print(f"Total de caracteres: {caracteres}")
    print(f"Total de palabras: {palabras}")
    print(f"Total de oraciones: {oraciones}")
    print(f"Palabra más larga: {mas_larga}")
    print(f"Palabra más corta: {mas_corta}")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")


if __name__ == "__main__":
    main()
