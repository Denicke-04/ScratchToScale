import os
import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2, prediction_service_pb2_grpc
import numpy as np
from PIL import Image
import requests
from io import BytesIO
from flask import Flask,request,jsonify

host = os.getenv('TF_CLOTHING_MODEL_HOST','localhost:8500')
channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)
pants_url = 'https://bit.ly/pants-test'
hat_url = 'https://bit.ly/hat-test'

app = Flask('gateway')

def preprocess_input(x):
    x /= 127.5
    x -= 1.
    return x

def np_to_protobuf(data):
    return tf.make_tensor_proto(data,shape = data.shape)

def convert_X_to_pb_request(X):
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = 'clothing-model'
    pb_request.model_spec.signature_name = 'serving_default'
    pb_request.inputs['input_8'].CopyFrom(np_to_protobuf(X))
    return pb_request


def preprocess_url(url):    
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to download image. Status code: {response.status_code}")
    with Image.open(BytesIO(response.content)) as img:
        img = img.resize((299, 299), Image.NEAREST)
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X= preprocess_input(X)
    return X

def merge_with_class(pb_response):
    classes = ['dress', 'hat', 'longsleeve', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']
    raw_output = pb_response.outputs["dense_7"].float_val
    output_array = np.array(raw_output)
    pred_index = np.argmax(output_array)
    predicted_class = classes[pred_index].capitalize()
    predicted_score = output_array[pred_index]
    return predicted_class, predicted_score

def perform_classification(url):
    X = preprocess_url(url)
    pb_request = convert_X_to_pb_request(X)
    pb_response = stub.Predict(pb_request,timeout = 20.0)
    predicted_class, predicted_score = merge_with_class(pb_response)
    return f"Predicted class: {predicted_class} (score: {predicted_score:.4f})"

@app.route('/predict',methods = ['POST'])
def predict():
    data = request.get_json()
    url = data.get('url')
    result = perform_classification(url)
    return jsonify(result)

if __name__ == "__main__":
    #url = pants_url
    #result = perform_classification(url)
    #print(result)
    app.run(debug = True, host = '0.0.0.0', port = 9600)



