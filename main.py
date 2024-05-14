# Bergamasco Jacopo, 4AIA, A.S. 2023-2024

# TODO: Separare un po' di schifezze per fare ordine

DEBUG = False

if DEBUG:
    from debug import *

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

def get_data(images_path: str, labels_path: str, cap: int = None) -> tuple[list[list[list[int]]], list[int]]:
    return (read_images(images_path, cap), read_labels(labels_path, cap))

def flatten(matrix: list[list[int]]) -> list[int]:
    # STANNO INIZIANDO A FARMI IMPAZZIRE
    return [pixel for row in matrix for pixel in row]

def extract_features(images: list[list[list[int]]]) -> list[list[int]]:
    return [flatten(img) for img in images]

def distance(a: list[int], b: list[int]) -> int:
    return sum(
        [
            (x - y) ** 2 for x, y in zip(a, b)
        ]
    ) ** 0.5

def training_distances(test_img: list[int], train_images: list[int]) -> list[int]:
    return [distance(test_img, train_img) for train_img in train_images]

def most_frequent(candidates: list[int]) -> int:
    freqs = [0 for i in range(10)]
    for n in candidates:
        freqs[n] += 1
    return sorted(enumerate(freqs), key=lambda x: x[1], reverse=True)[0][0]

def knn(train_images: list[list[int]], train_labels: list[int], test_images: list[list[int]], k: int = 3):
    predicted = []
    for test_img in test_images:
        train_dists = training_distances(test_img, train_images)
        sorted_dists_idx = [
            pair[0] for pair in sorted(enumerate(train_dists), key=lambda x: x[1])    
        ]
        candidates = [train_labels[i] for i in sorted_dists_idx[:k]]
        predicted.append(most_frequent(candidates))
    return predicted

if __name__ == "__main__":
    print("Avvio lettura dati di training...")
    (train_images, train_labels) = get_data(DATA_FILENAMES["TRAIN_IMAGES"], DATA_FILENAMES["TRAIN_LABELS"], 1000)
    print("Dati di training letti correttamente!")
    print("Avvio lettura dati di test...")
    (test_images, test_labels) = get_data(DATA_FILENAMES["TEST_IMAGES"], DATA_FILENAMES["TEST_LABELS"], 30)
    print("Dati di test letti correttamente!")
    print("Avvio calcolo...")
    compute = knn(extract_features(train_images), train_labels, extract_features(test_images), 7)
    print(compute)
    print(len(compute))