# Bergamasco Jacopo, 4AIA, A.S. 2023-2024
# ocr.py -> Funzioni principali

DEBUG = False

from src.data_from_files import get_data
from src.image_computation import extract_features
from src.knn import knn
if DEBUG:
    from src.debug import *

DATA_DIR = "data"
DATA_FILENAMES = {
    "TEST_IMAGES":  f"{DATA_DIR}/t10k-images.idx3-ubyte",
    "TEST_LABELS":  f"{DATA_DIR}/t10k-labels.idx1-ubyte",
    "TRAIN_IMAGES": f"{DATA_DIR}/train-images.idx3-ubyte",
    "TRAIN_LABELS": f"{DATA_DIR}/train-labels.idx1-ubyte"
}

if __name__ == "__main__":
    print("Avvio lettura dati di training...")
    (train_images, train_labels) = get_data(DATA_FILENAMES["TRAIN_IMAGES"], DATA_FILENAMES["TRAIN_LABELS"], 1000)
    print("Dati di training letti correttamente!")

    print("Avvio lettura dati di test...")
    (test_images, test_labels) = get_data(DATA_FILENAMES["TEST_IMAGES"], DATA_FILENAMES["TEST_LABELS"], 30)
    print("Dati di test letti correttamente!")
    
    print("Avvio calcolo...")
    compute = knn(extract_features(train_images), train_labels, extract_features(test_images), 7)
    print("Calcolo completato!")