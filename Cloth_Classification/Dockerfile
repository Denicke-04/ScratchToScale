FROM public.ecr.aws/lambda/python:3.12
RUN pip install ai-edge-litert
RUN pip install Pillow requests numpy
COPY ["lambda_function.py","clothing_model.tflite","./"]
CMD ["lambda_function.lambda_handler"]