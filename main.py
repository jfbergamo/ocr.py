# Bergamasco Jacopo, 4AIA, A.S. 2023-2024

DATA_FILENAMES = {
    "TEST_IMAGES": "data/t10k-images.idx3-ubyte",
    "TEST_LABELS": "data/t10k-labels.idx1-ubyte",
    "TRAIN_IMAGES": "data/train-images.idx3-ubyte",
    "TRAIN_LABELS": "data/train-labels.idx1-ubyte"
}

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


if __name__ == "__main__":
    print("Avvio lettura dati")
    test_labels = read_labels(DATA_FILENAMES["TEST_LABELS"])