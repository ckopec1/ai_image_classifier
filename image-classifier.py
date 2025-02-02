from flask import Flask, request, render_template, jsonify
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

def predict_image(img_path):
    # Load the image and resize it to the input size of the model (224x224)
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Make a prediction
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Format the predictions
    result = []
    for _, label, prob in decoded_predictions:
        result.append(f"{label} ({prob:.2f}%)")
    
    return result

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({"error": "No file part"})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"})
        
        if file:
            # Save the uploaded file temporarily
            img_path = "uploaded_image.jpg"
            file.save(img_path)
            
            # Predict the image content
            predictions = predict_image(img_path)
            
            # Remove the temporary file
            os.remove(img_path)
            
            return jsonify({"predictions": predictions})
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
