# Bergamasco Jacopo, 4AIA, A.S. 2023-2024
# data_from_files.py -> Legge immagini e etichette dal file binario

def bytes_be_to_int_le(byte: bytes) -> int:
    return int.from_bytes(byte, 'big')

def read_images(filename: str, cap: int = None) -> list[list[list[int]]]:
    images = []
    with open(filename, "rb") as f:
        __mn = f.read(4)
        _ = bytes_be_to_int_le(f.read(4))
        img_count  = cap if cap else _
        rows_count = bytes_be_to_int_le(f.read(4))
        cols_count = bytes_be_to_int_le(f.read(4))

        # BRUTTISSIMO MA MOSTRA LA MAGIA DEL PITONE
        images = [[[bytes_be_to_int_le(f.read(1)) for col in range(cols_count)] for row in range(rows_count)] for img in range(img_count)]

    return images
        
def read_labels(filename: str, cap: int = None) -> list[int]:
    labels = []
    with open(filename, "rb") as f:
        __mn = f.read(4)
        items_count = bytes_be_to_int_le(f.read(4))
        labels = [bytes_be_to_int_le(f.read(1)) for label in range(items_count)]
    return labels

def get_data(images_path: str, labels_path: str, cap: int = None) -> tuple[list[list[list[int]]], list[int]]:
    return (read_images(images_path, cap), read_labels(labels_path, cap))