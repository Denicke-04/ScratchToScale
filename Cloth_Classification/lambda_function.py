# ### TFLite Model Inference Script
from PIL import Image
import requests
from io import BytesIO
import numpy as np
from ai_edge_litert.interpreter import Interpreter

interpreter = Interpreter(model_path = 'clothing_model.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index'] 

pants_url = 'https://bit.ly/pants-test'
hat_url = 'https://bit.ly/hat-test'
    
def preprocess_input(x):
    x /= 127.5
    x -= 1.
    return x

def predict(custom_url = pants_url):
    response = requests.get(custom_url)
    if response.status_code != 200:
        raise ValueError(f"Failed to download image. Status code: {response.status_code}")
    with Image.open(BytesIO(response.content)) as img:
        img = img.resize((299, 299), Image.NEAREST)
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X= preprocess_input(X)
    
    interpreter.set_tensor(input_index,X)
    interpreter.invoke()
    output = interpreter.get_tensor(output_index)
    classes = ['dress', 'hat', 'longsleeve', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']
    pred_index = np.argmax(output[0])
    predicted_class = classes[pred_index].capitalize()
    predicted_score = output[0][pred_index]
    return (f"Predicted class: {predicted_class} (score: {predicted_score:.4f})")

def lambda_handler(event,context = None):
    url = event.get('url', pants_url)
    try:
        result = predict(url)
        return result
    except Exception as e:
        return f"Error: {str(e)}"