from flask import Flask, render_template, request
from learner import save_training_data, predict_image, count_data
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html", data=count_data())


@app.route("/train", methods=["GET", "POST"])
def train():
    if request.method == "POST":
        label = request.form.get("label")
        file = request.files.get("image")

        if not label or not file:
            return render_template("train.html", error="⚠️ Fill all fields", data=count_data())

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        save_training_data(label, path)

        return render_template("train.html", success="✅ Learned!", data=count_data())

    return render_template("train.html", data=count_data())


@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("image")

    if not file:
        return render_template("index.html", error="⚠️ Upload image", data=count_data())

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    label, confidence = predict_image(path)

    return render_template("result.html", image=path, label=label, confidence=confidence)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
