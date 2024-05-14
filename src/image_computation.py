# Bergamasco Jacopo, 4AIA, A.S. 2023-2024
# image_computation.py -> Esegue operazioni sulle immagini

def flatten(matrix: list[list[int]]) -> list[int]:
    # STANNO INIZIANDO A FARMI IMPAZZIRE
    return [pixel for row in matrix for pixel in row]

def extract_features(images: list[list[list[int]]]) -> list[list[int]]:
    return [flatten(img) for img in images]

def distance(a: list[int], b: list[int]) -> int:
    return sum( [(x - y) ** 2 for x, y in zip(a, b)] ) ** 0.5