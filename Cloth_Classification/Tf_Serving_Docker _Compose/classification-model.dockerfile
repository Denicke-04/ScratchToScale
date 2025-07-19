FROM tensorflow/serving:2.19.0
COPY xception_v1_34_0.883 /models/clothing-model/1
ENV MODEL_NAME="clothing-model"