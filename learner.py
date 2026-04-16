import os
import numpy as np
from PIL import Image

DATASET_PATH = "data"
os.makedirs(DATASET_PATH, exist_ok=True)

THRESHOLD = 0.45


# ✅ SAVE TRAINING DATA
def save_training_data(label, image_path):
    label_path = os.path.join(DATASET_PATH, label)
    os.makedirs(label_path, exist_ok=True)

    filename = os.path.basename(image_path)
    Image.open(image_path).save(os.path.join(label_path, filename))


# ✅ COUNT DATA
def count_data():
    counts = {}
    for label in os.listdir(DATASET_PATH):
        counts[label] = len(os.listdir(os.path.join(DATASET_PATH, label)))
    return counts


# ✅ PREPROCESS IMAGE
def preprocess(path):
    img = Image.open(path).convert("L").resize((64, 64))
    img = np.array(img) / 255.0
    return img.flatten()


# ✅ COMPARE HISTOGRAM
def compare(img1, img2):
    hist1, _ = np.histogram(img1, bins=50, range=(0, 1))
    hist2, _ = np.histogram(img2, bins=50, range=(0, 1))

    hist1 = hist1 / np.sum(hist1)
    hist2 = hist2 / np.sum(hist2)

    return np.sum(np.minimum(hist1, hist2))


def predict_image(image_path):
    try:
        input_img = preprocess(image_path)

        best_label = None
        best_score = 0

        for label in os.listdir(DATASET_PATH):
            scores = []

            for file in os.listdir(os.path.join(DATASET_PATH, label)):
                path = os.path.join(DATASET_PATH, label, file)
                stored_img = preprocess(path)

                score = compare(input_img, stored_img)
                scores.append(score)

            if len(scores) < 2:
                continue  # 🔥 skip weak dataset

            top_score = max(scores)   # 🔥 IMPORTANT CHANGE

            if top_score > best_score:
                best_score = top_score
                best_label = label

        # 🔥 STRONG UNKNOWN FILTER
        if best_score < 0.55:
            return "Unknown ❓", round(best_score * 100, 2)

        # 🔥 LOW CONFIDENCE RANGE
        if best_score < 0.65:
            return best_label + " (Low Confidence)", round(best_score * 100, 2)

        return best_label, round(best_score * 100, 2)

    except Exception as e:
        print(e)
        return "Error", 0