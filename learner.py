import os
import numpy as np
from PIL import Image

DATASET_PATH = "data"
os.makedirs(DATASET_PATH, exist_ok=True)

THRESHOLD = 0.55


# ✅ SAVE TRAINING DATA
def save_training_data(label, image_path):
    label_path = os.path.join(DATASET_PATH, label)
    os.makedirs(label_path, exist_ok=True)

    filename = os.path.basename(image_path)
    Image.open(image_path).save(os.path.join(label_path, filename))


# ✅ COUNT DATA (FIXED FOR .gitkeep)
def count_data():
    counts = {}

    for label in os.listdir(DATASET_PATH):
        label_path = os.path.join(DATASET_PATH, label)

        # 🔥 ignore files like .gitkeep
        if not os.path.isdir(label_path):
            continue

        counts[label] = len(os.listdir(label_path))

    return counts


# ✅ PREPROCESS
def preprocess(path):
    img = Image.open(path).convert("L").resize((64, 64))
    img = np.array(img) / 255.0
    return img.flatten()


# ✅ COMPARE
def compare(img1, img2):
    hist1, _ = np.histogram(img1, bins=50, range=(0, 1))
    hist2, _ = np.histogram(img2, bins=50, range=(0, 1))

    hist1 = hist1 / np.sum(hist1)
    hist2 = hist2 / np.sum(hist2)

    return np.sum(np.minimum(hist1, hist2))


# ✅ PREDICT (FULL FIXED)
def predict_image(image_path):
    try:
        input_img = preprocess(image_path)

        best_label = None
        best_score = 0

        for label in os.listdir(DATASET_PATH):
            label_path = os.path.join(DATASET_PATH, label)

            # 🔥 skip .gitkeep
            if not os.path.isdir(label_path):
                continue

            scores = []

            for file in os.listdir(label_path):
                path = os.path.join(label_path, file)
                stored_img = preprocess(path)

                score = compare(input_img, stored_img)
                scores.append(score)

            if len(scores) < 2:
                continue

            top_score = max(scores)

            if top_score > best_score:
                best_score = top_score
                best_label = label

        # 🔥 UNKNOWN
        if best_score < 0.55:
            return "Unknown ❓", round(best_score * 100, 2)

        # 🔥 LOW CONFIDENCE
        if best_score < 0.65:
            return best_label + " (Low Confidence)", round(best_score * 100, 2)

        return best_label, round(best_score * 100, 2)

    except Exception as e:
        print("ERROR:", e)
        return "Error", 0
