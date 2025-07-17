from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

target_names = ['Setosa', 'Versicolor', 'Virginica']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        float(data['sepal_length']),
        float(data['sepal_width']),
        float(data['petal_length']),
        float(data['petal_width'])
    ]
    prediction = model.predict([features])[0]
    class_label = target_names[prediction]  
    return jsonify({'prediction': class_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
