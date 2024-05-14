# Bergamasco Jacopo, 4AIA, A.S. 2023-2024
# knn.py -> Esegue i calcoli dell'algoritmo knn

from src.image_computation import distance

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